import requests
import pytest
from utils.logger import logger

# Obtener usuario GET:
def test_get_user(url_base, header_request):
    url = f"{url_base}/2"
    logger.info("== Inicio test_get_user ==")
    logger.info("Preparando GET %s", url)

    try:
        logger.info("Headers: %s", header_request)
        response = requests.get(url, headers=header_request, timeout=10)
        logger.info("Respuesta: status=%d", response.status_code)

        assert response.status_code == 200, "El GET /2 deberia responder 200"

        data = response.json()
        logger.info("Payload recibido (resumen): id=%s, email=%s",
                    data.get("data", {}).get("id"),
                    data.get("data", {}).get("email"))

        assert data["data"]["id"] == 2, "El id del usuario debe ser 2"

        logger.info("test_get_user completado con éxito")
    except AssertionError as ae:
        logger.error("Fallo una asercion en test_get_user: %s", ae)
        raise
    except Exception as e:
        logger.exception("Error inesperado en test_get_user: %s", e)
        raise
    finally:
        logger.info("== Fin test_get_user ==")


# Crear usuario POST:
def test_create_user(url_base, header_request):
    url = url_base
    payload = {"name": "Penelope", "job": "QA Tester"}

    logger.info("== Inicio test_create_user ==")
    logger.info("Preparando POST %s", url)
    logger.info("Payload: %s", payload)

    try:
        logger.info("Headers: %s", header_request)
        response = requests.post(url, headers=header_request, json=payload, timeout=10)
        logger.info("Respuesta: status=%d", response.status_code)

        assert response.status_code == 201, "El POST debe responder 201 (creado)"

        data = response.json()
        logger.info("Payload recibido (resumen): name=%s, job=%s, id=%s, createdAt=%s",
                    data.get("name"),
                    data.get("job"),
                    data.get("id"),
                    data.get("createdAt"))

        assert data["name"] == payload["name"], "El nombre devuelto debe coincidir"

        logger.info("test_create_user completado con exito")
    except AssertionError as ae:
        logger.error("Fallo una asercion en test_create_user: %s", ae)
        raise
    except Exception as e:
        logger.exception("Error inesperado en test_create_user: %s", e)
        raise
    finally:
        logger.info("== Fin test_create_user ==")


# Eliminar registro DELETE:
def test_delete_user(url_base, header_request):
    url = f"{url_base}/2"
    logger.info("== Inicio test_delete_user ==")
    logger.info("Preparando DELETE %s", url)

    try:
        logger.info("Headers: %s", header_request)
        response = requests.delete(url, headers=header_request, timeout=10)
        logger.info("Respuesta: status=%d", response.status_code)

        assert response.status_code == 204, "El DELETE /2 debe responder 204"

        logger.info("test_delete_user completado con exito")
    except AssertionError as ae:
        logger.error("Fallo una asercion en test_delete_user: %s", ae)
        raise
    except Exception as e:
        logger.exception("Error inesperado en test_delete_user: %s", e)
        raise
    finally:
        logger.info("== Fin test_delete_user ==")
