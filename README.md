# CLI calculator

Простой консольный калькулятор с поддержкой базовых арифметических операций.
.
---
## Запуск
Интерактивный режим 
```bash
python main.py
```
## Команды

| Команда  | Описание               | Пример       |
|----------|------------------------|--------------|
| add a b  | Сложение               | add 2 3 → 5  |
| sub a b  | Вычитание              | sub 7 2 → 5  |
| mult a b | Умножение              | mult 4 2 → 8 |
| div a b  | Деление                | div 10 2 → 5 |
| help     | Показать список команд | help         |
| exit     | Завершить программу    | exit         |

## Тесты
Запуск тестов через pytest:
```commandline
make test
```

## Makefile
```bash
make run    # запуск приложения
make test   # запуск тестов
make lint   # проверка типизации через mypy
```

## Технологии
	•	Python 3.11+
	•	pytest
	•	mypy

## Структура проекта.
```commandline
cli_calculator/
├── Makefile
├── README.md
├── __init__.py
├── calculator.py          # Логика вычислений
├── cli.py                 # CLI-интерфейс (App)
├── main.py                # Точка входа
├── utils/
│   ├── __init__.py
│   └── logger.py          # Настройка логирования
└── tests/
    ├── __init__.py
    └── test_cli_calculator.py  # Юнит-тесты
```
