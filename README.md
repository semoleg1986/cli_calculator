# CLI calculator

Простой консольный калькулятор с поддержкой базовых арифметических операций.
.
---
## Запуск
Интерактивный режим 
```bash
python main.py
```

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
