#!/bin/bash

echo "🚀 Ejecutando pipeline ETL..."
echo

# Verificar si existe al menos un CSV en data/raw
if [ ! -f "data/raw/ventas_sucursal1.csv" ]; then
    echo "⚠️  Advertencia: No se encontró data/raw/ventas_sucursal1.csv"
    echo "   Crea al menos un archivo CSV en data/raw/ para procesar."
    exit 1
fi

# Crear carpetas si no existen
mkdir -p data/processed logs

# Ejecutar el pipeline
python3 src/etl_pipeline.py

if [ $? -eq 0 ]; then
    echo
    echo "✅ Pipeline finalizado correctamente."
    echo "Resultados en: data/processed/"
else
    echo
    echo "❌ El pipeline falló. Revisa los logs en la carpeta 'logs'."
fi
