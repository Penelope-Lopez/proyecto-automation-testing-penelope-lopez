from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario,password", [("standard_user", "secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    driver = login_in_driver

    LoginPage(driver).login_completo(usuario,password)

    inventory_page = InventoryPage(driver)

    logger.info("== Inicio test_cart ==")
    logger.info("Usuario configurado: %s", usuario)

    try:
        logger.info("Agregando el primer producto al carrito desde Inventory")
        inventory_page.agregar_primer_producto()

        logger.info("Abriendo la vista del carrito")
        inventory_page.abrir_carrito()

        logger.info("Validando productos presentes en el carrito")
        cart_page = CartPage(driver)
        productos_en_carrito = cart_page.obtener_productos_carrito()
        logger.info("Cantidad de productos en el carrito: %d", len(productos_en_carrito))

        assert len(productos_en_carrito) == 20, "El carrito debería tener exactamente 1 producto después de agregar el primero"
        #assert False, "Fallo de prueba forzado"

        # (Opcional) Log de detalle del producto si tu método lo permite:
        # logger.info("Producto en carrito: %s", productos_en_carrito[0].texto_titulo())

        logger.info("Test de carrito completado correctamente")

    # except AssertionError as ae:
    #     logger.error("Fallo una aserción en test_cart: %s", ae)
    #     raise
    except Exception as e:
        # logger.exception agrega el stack trace automaticamente
        logger.exception("Error inesperado en test_cart: %s", e)
        raise
    # finally:
        # Dejar este bloque solo si tu fixture no cierra el driver
        try:
            driver.quit()
            logger.info("Driver cerrado desde test_cart")
        except Exception as e:
            logger.warning("No se pudo cerrar el driver en test_cart: %s", e)

    logger.info("== Fin test_cart ==")
