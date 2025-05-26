# test_solution
# Тестовое для Солюшен

Скрипт выполняет парсинг карточки товара с Wildberries по его артикулу.

Реализована функция:
```
def get_wb_info(article: str) -> Optional[dict]:
```
Функция принимает артикул товара Wildberries (например, 400682365) и возвращает словарь с названием и ценой товара:
```
{'name': 'Название товара', 'price': 1599}
```
Если товар не найден — возвращается None.

Парсинг реализован с использованием HTTP-запроса к открытому API Wildberries (без Selenium).

Код структурирован: основная логика вынесена в отдельную функцию.

В проекте присутствуют как юнит-тесты (с моками), так и интеграционные тесты (с реальными запросами).

## Технологический стек
- Python 3.12
- requests

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:dariazueva/test_solution.git
```

```bash
cd test_solution
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

* Если у вас Linux/macOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/Scripts/activate
    ```

```bash
python -m pip install --upgrade pip
```

Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

Запуск тестов и самого скрипта через терминал:

```bash
python  wb_parse.py 
```

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/