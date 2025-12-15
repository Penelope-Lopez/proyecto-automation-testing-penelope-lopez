from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login
from utils.logger import logger

@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    logger.info("== Inicio test_login_validation ==")
    logger.info("Completando con los datos de usuarios (desde CSV)")
    logger.info("Usuario: %s | debe_funcionar: %s", usuario, debe_funcionar)

    driver = login_in_driver

    LoginPage(driver).login_completo(usuario,password)

    try:
        
        if debe_funcionar is True:
            logger.info("Verificando redireccionamiento dentro de la pagina")
            current = driver.current_url
            logger.info("URL actual: %s", current)
            assert "/inventory.html" in current, "No se redirigio al inventario"
            logger.info("Test de login (caso valido) completado")
        else:
            logger.info("Verificando mensaje de error de login para credenciales invalidas")
            mensaje_error = LoginPage(driver).obtener_error()
            logger.info("Mensaje de error obtenido: %s", mensaje_error)
            assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando"
            logger.info("Test de login (caso inválido) completado")

    except AssertionError as ae:
        logger.error("Fallo una asercion en test_login_validation: %s", ae)
        raise
    except Exception as e:
        # Adjunta stack trace automáticamente
        logger.exception("Error inesperado en test_login_validation: %s", e)
        raise
    finally:

        pass

    logger.info("== Fin test_login_validation ==")
