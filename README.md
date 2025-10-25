# Word Analyzer CLI

Простой CLI-инструмент для анализа текста.  
Позволяет подсчитать общее количество слов, количество уникальных слов и вывести топ-N самых часто встречающихся слов.
---
## Запуск
1. Ручной ввод текста
```bash
python main.py
```
2. Запуск с аргументами
```bash
python main.py --file test.txt --top 10
```
	•	--file — путь к текстовому файлу
	•	--top — количество слов в топе (по умолчанию 5)

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
	•	argparse
	•	tabulate
	•	pytest
	•	mypy

## Структура проекта.
```commandline
word_analyzer/
├── Makefile
├── README.md
├── init.py
├── analyzer.py          # Логика анализа текста
├── cli.py               # CLI интерфейс приложения
├── main.py              # Точка входа
├── test.txt             # Пример текстового файла
├── tests/               # Тесты
│   └── test_analyzer.py
└── utils/
    └── logger.py        # Логирование
```
