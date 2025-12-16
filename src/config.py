import os
from pathlib import Path

# Configuración de rutas (adaptable a entornos sin cloud)
DATA_RAW = Path("data/raw")
DATA_PROCESSED = Path("data/processed")
LOGS_DIR = Path("logs")

# Crear carpetas si no existen
for p in [DATA_PROCESSED, LOGS_DIR]:
    p.mkdir(parents=True, exist_ok=True)
