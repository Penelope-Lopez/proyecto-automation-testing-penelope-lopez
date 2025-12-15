from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from faker import Faker
from utils.logger import logger

# Inicializamos Faker:
fake = Faker()

@pytest.mark.parametrize("usuario,password,debe_funcionar", [
     (fake.user_name(), fake.password(), False),
     (fake.user_name(), fake.password(), False),
])
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    driver = login_in_driver

    LoginPage(driver).login_completo(usuario,password)

    logger.info("== Inicio test_login_faker ==")
    logger.info("Completando con los datos de usuarios (Faker)")
    logger.info("Usuario generado: %s | debe_funcionar: %s", usuario, debe_funcionar)
    
    try:
        if debe_funcionar is True:
            logger.info("Verificando redireccionamiento dentro de la pagina")
            assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
            logger.info("Test de login_faker (caso valido) completado")
        else:
            logger.info("Verificando mensaje de error de login para credenciales inválidas")
            mensaje_error = LoginPage(driver).obtener_error()
            logger.info("Mensaje de error obtenido: %s", mensaje_error)
            assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando"
            logger.info("Test de login_faker (caso inválido) completado")

    except AssertionError as ae:
        logger.error("Fallo una asercion en test_login_faker: %s", ae)
        raise
    except Exception as e:
        logger.exception("Error inesperado en test_login_faker: %s", e)
        raise
