
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos
from utils.logger import logger
import time
from pages.login_page import LoginPage

RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password", [("standard_user", "secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver, usuario, password, nombre_producto):
    driver = login_in_driver
    LoginPage(driver).login_completo(usuario,password)
    inventory_page = InventoryPage(driver)

    logger.info("== Inicio test_cart_json ==")
    logger.info("Usuario configurado: %s", usuario)
    logger.info("Producto objetivo (desde JSON): %s", nombre_producto)

    try:
        logger.info("Agregando el producto al carrito por nombre: %s", nombre_producto)
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        logger.info("Abriendo la vista del carrito")
        inventory_page.abrir_carrito()

        logger.info("Esperando a que el carrito esté visible (sleep corto)")
        time.sleep(1)

        logger.info("Validando que el producto en el carrito coincide con el objetivo")
        cart_page = CartPage(driver)
        nombre_en_carrito = cart_page.obtener_nombre_producto_carrito()
        logger.info("Producto encontrado en carrito: %s", nombre_en_carrito)

        assert nombre_en_carrito == nombre_producto, (
            f"Se esperaba '{nombre_producto}' en el carrito, "
            f"pero se encontró '{nombre_en_carrito}'"
        )

        logger.info("Test de carrito con JSON completado correctamente")

    except AssertionError as ae:
        logger.error("Falló una aserción en test_cart_json: %s", ae)
        raise
    except Exception as e:
        logger.exception("Error inesperado en test_cart_json: %s", e)
        raise
    finally:
        # Dejar solo si tu fixture no cierra el driver
        try:
            driver.quit()
            logger.info("Driver cerrado desde test_cart_json")
        except Exception as e:
            logger.warning("No se pudo cerrar el driver en test_cart_json: %s", e)
