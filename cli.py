from calculator import Calculator

class App:
    """
    CLI-приложение
    """

    COMMANDS = {
        "add": "сложение a + b",
        "sub": "вычитание a - b",
        "mult": "умножение a * b",
        "div": "деление a / b",
        "help": "показать список команд",
        "exit": "выйти из программы",
    }

    operator = {
        "add": "+",
        "sub": "-",
        "mult": "*",
        "div": "/",
    }

    def __init__(self, calculator_cls=Calculator) -> None:
        self.running = True
        self.calculator_cls = calculator_cls

    def run(self) -> None:
        print("Введите 'help' для списка команд.")
        while self.running:
            try:
                cmd: list[str] = input("> ").strip().lower().split()
                if not cmd:
                    print("Пустая команда")
                    continue

                command = cmd[0]
                match command:
                    case "exit":
                        self.exit()
                    case "help":
                        self.print_help()
                    case "add" | "sub" | "mult" | "div":
                        if len(cmd) != 3:
                            print("Ошибка: Пример: add 2 3")
                            continue
                        a, b = self._parse_args(cmd[1], cmd[2])
                        calc = self.calculator_cls(a, b)
                        operation = getattr(calc, command)
                        result = operation()

                        print(f"Результат: {result}")
                    case _:
                        print(f'"{command}" такой команды нет')
            except ValueError as e:
                print("Ошибка:", e)
            except ZeroDivisionError as e:
                print("Ошибка:", e)
            except Exception as e:
                print("Неожиданная ошибка:", e)


    @staticmethod
    def _parse_args(a_str: str, b_str: str) -> tuple[float, float]:
        """Преобразование введённых аргументов в числа"""
        try:
            return float(a_str), float(b_str)
        except ValueError:
            raise ValueError("Аргументы должны быть числами")

    def print_help(self) -> None:
        """Вывод списка команд"""
        print("\nДоступные команды:")
        for cmd, desc in self.COMMANDS.items():
            print(f"  {cmd:<6} - {desc}")
        print()

    def exit(self):
        print("Программа завершена")
        self.running = False
