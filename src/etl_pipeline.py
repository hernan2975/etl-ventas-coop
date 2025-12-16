import pandas as pd
import numpy as np
from pathlib import Path
from .config import DATA_RAW, DATA_PROCESSED
from .utils import setup_logger

logger = setup_logger("ETL")

def extract():
    """Extrae datos desde múltiples CSV (simulando sucursales)."""
    files = list(DATA_RAW.glob("ventas_*.csv"))
    if not files:
        logger.warning("⚠️ No se encontraron archivos en data/raw/")
        return None
    
    dfs = []
    for f in files:
        try:
            df = pd.read_csv(f, encoding="utf-8", sep=",")
            df["origen"] = f.stem
            dfs.append(df)
            logger.info(f"✅ Cargado: {f.name} ({len(df)} filas)")
        except Exception as e:
            logger.error(f"❌ Error al cargar {f.name}: {e}")
    return pd.concat(dfs, ignore_index=True) if dfs else None

def transform(df: pd.DataFrame):
    """Limpieza y enriquecimiento básico."""
    try:
        # Eliminar duplicados y nulos críticos
        df = df.drop_duplicates()
        df = df.dropna(subset=["fecha", "producto", "cantidad", "precio_unitario"])
        
        # Tipos de dato
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
        df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
        df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")
        
        # Calcular importe
        df["importe"] = df["cantidad"] * df["precio_unitario"]
        
        # Filtrar fechas válidas y cantidades > 0
        df = df[(df["fecha"].notna()) & (df["cantidad"] > 0) & (df["importe"] > 0)]
        
        logger.info(f"	Transformado: {len(df)} filas válidas")
        return df
    except Exception as e:
        logger.error(f"❌ Error en transformación: {e}")
        return None

def load(df: pd.DataFrame):
    """Carga en formato eficiente (Parquet) y CSV legible."""
    try:
        output_parquet = DATA_PROCESSED / "ventas_consolidadas.parquet"
        output_csv = DATA_PROCESSED / "ventas_consolidadas.csv"
        
        df.to_parquet(output_parquet, index=False)
        df.to_csv(output_csv, index=False, encoding="utf-8")
        
        logger.info(f"✅ Guardado: {output_parquet.name} y {output_csv.name}")
        return True
    except Exception as e:
        logger.error(f"❌ Error al guardar: {e}")
        return False

def run_etl():
    logger.info("🚀 Iniciando pipeline ETL...")
    df = extract()
    if df is None or df.empty:
        logger.warning("⚠️ Pipeline detenido: sin datos para procesar.")
        return False
    df_clean = transform(df)
    if df_clean is None:
        return False
    success = load(df_clean)
    logger.info("🏁 Pipeline finalizado." if success else "💥 Pipeline fallido.")
    return success

if __name__ == "__main__":
    run_etl()
