import logging
import pathlib

# Directorio de logs:
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

# Archivo de logs:
log_file = audit_dir/ 'suite.log'

# Instanciar logger:
logger = logging.getLogger("ProyectoAtomationPenelopeLopez")
logger.setLevel(logging.INFO)

# Evitar duplicar handlers si el modulo se importa mas de una vez:
if not logger.handlers:

    # Handler a archivo:
    file_handler = logging.FileHandler(str(log_file), mode="a", encoding="utf-8")

    # Formatter (con parentesis y coma entre argumentos):
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Aplicar formatter y registrar handler:
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
