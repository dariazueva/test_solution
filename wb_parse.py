import unittest
from typing import Optional
from unittest.mock import Mock, patch

import requests

BASE_URL = "https://card.wb.ru/cards/v1/detail"


def get_wb_info(article: str) -> Optional[dict]:
    """Получает название и цену товара с Wildberries по его артикулу.

    :param article: Артикул товара (например, '400682365')
    :return: Словарь с ключами 'name' и 'price' или None, если товар не найден
    """
    try:
        url = f"{BASE_URL}?appType=1&curr=rub&dest=12358530&nm={article}"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        data = response.json()
        products = data.get("data", {}).get("products", [])
        if not products:
            return None
        product = products[0]
        name = product.get("name")
        price = product.get("salePriceU", 0) // 100
        return {"name": name, "price": price}
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


class TestGetWbInfo(unittest.TestCase):

    @patch("requests.get")
    def test_successful_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "products": [
                    {
                        "name": "Тестовый товар",
                        "salePriceU": 159900,
                    }
                ]
            }
        }
        mock_get.return_value = mock_response
        result = get_wb_info("123456")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Тестовый товар")
        self.assertEqual(result["price"], 1599)

    @patch("requests.get")
    def test_product_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": {"products": []}}
        mock_get.return_value = mock_response

        result = get_wb_info("000000")
        self.assertIsNone(result)


class TestGetWbInfoIntegration(unittest.TestCase):

    def test_real_article(self):
        """Проверяет, что функция возвращает данные по реальному артикулу."""
        result = get_wb_info("400682365")
        self.assertIsNotNone(result)
        self.assertIn("name", result)
        self.assertIn("price", result)

    def test_nonexistent_article(self):
        result = get_wb_info("9999999999999")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
