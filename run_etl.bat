@echo off
echo 🚀 Ejecutando pipeline ETL...
echo.

REM Verificar si existe la carpeta data/raw
if not exist "data\raw\ventas_sucursal1.csv" (
    echo ⚠️  Advertencia: No se encontró data\raw\ventas_sucursal1.csv
    echo    Crea al menos un archivo CSV en data\raw\ para procesar.
    pause
    exit /b 1
)

REM Crear carpetas si no existen
if not exist "data\processed" mkdir "data\processed"
if not exist "logs" mkdir "logs"

REM Ejecutar el pipeline
python src\etl_pipeline.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ Pipeline finalizado correctamente.
    echo Resultados en: data\processed\
) else (
    echo.
    echo ❌ El pipeline falló. Revisa los logs en la carpeta 'logs'.
)

pause
