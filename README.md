# 📊 ETL Ventas Cooperativa  
_Pipeline robusto para consolidación de ventas en entornos con conectividad intermitente_

## ✅ Características
- **Resiliente**: maneja archivos faltantes, formatos corruptos y errores de lectura.
- **Auditado**: logging detallado (archivo + consola).
- **Portátil**: sin dependencias de red, cloud o bases externas.
- **Eficiente**: salida en Parquet (compacto) + CSV (legible).

## ▶️ Cómo ejecutar
```bash
pip install -r requirements.txt
python src/etl_pipeline.py
