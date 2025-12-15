
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from utils.logger import logger
from pages.inventory_page import InventoryPage 
from pages.cart_page import CartPage 
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario,password", [("standard_user", "secret_sauce")])
def test_inventory(login_in_driver, usuario, password):
    driver = login_in_driver

    LoginPage(driver).login_completo(usuario,password)

    inventory_page = InventoryPage(driver)

    logger.info("== Inicio test_inventory ==")
    logger.info("Usuario configurado: %s", usuario)

    try:
        logger.info("Verificando que el inventario tiene productos disponibles")
        productos = inventory_page.obtener_todos_los_productos()
        logger.info("Cantidad de productos encontrados: %d", len(productos))
        assert len(productos) > 0, "El inventario está vacío"

        logger.info("Verificando que el carrito esté vacío al inicio")
        conteo_inicial = inventory_page.obtener_conteo_carrito()
        logger.info("Conteo inicial del carrito: %d", conteo_inicial)
        assert conteo_inicial == 0, "El carrito no está vacío al iniciar"

        logger.info("Agregando el primer producto al carrito")
        inventory_page.agregar_primer_producto()

        logger.info("Verificando contador del carrito después de agregar un producto")
        conteo_final = inventory_page.obtener_conteo_carrito()
        logger.info("Conteo final del carrito: %d", conteo_final)
        assert conteo_final == 1, "El contador del carrito debería ser 1"

        logger.info("Test de inventario completado correctamente")

    except AssertionError as ae:
        logger.error("Falló una aserción en test_inventory: %s", ae)
        # Re-lanzamos para que pytest marque el test como fallo
        raise
    except Exception as e:
        logger.exception("Error inesperado en test_inventory: %s", e)
        raise
    finally:
        # Si tu fixture cierra el driver automáticamente, podés remover esta línea.
        # Si NO lo hace, mantener el quit.
        try:
            driver.quit()
            logger.info("Driver cerrado desde test_inventory")
        except Exception as e:
            logger.warning("No se pudo cerrar el driver en test_inventory: %s", e)

  
