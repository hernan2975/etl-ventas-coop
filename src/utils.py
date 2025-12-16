import logging
from datetime import datetime
from pathlib import Path

def setup_logger(name: str) -> logging.Logger:
    """Configura logger con rotación por fecha y formato profesional."""
    log_file = Path("logs") / f"etl_{datetime.now().strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()  # también muestra en consola
        ]
    )
    return logging.getLogger(name)
