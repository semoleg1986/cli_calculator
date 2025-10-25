import builtins
import pytest
from unittest.mock import patch, MagicMock

from cli import App


@pytest.fixture
def mock_calc():
    """Мокаем класс Calculator."""
    mock_class = MagicMock()
    instance = mock_class.return_value
    instance.add.return_value = 5
    instance.sub.return_value = 1
    instance.mult.return_value = 6
    instance.div.return_value = 2
    return mock_class


def test_parse_args_success():
    assert App._parse_args("2", "3") == (2.0, 3.0)


def test_parse_args_invalid():
    with pytest.raises(ValueError, match="Аргументы должны быть числами"):
        App._parse_args("a", "2")


def test_print_help(capsys):
    app = App()
    app.print_help()
    captured = capsys.readouterr()
    assert "Доступные команды" in captured.out
    assert "add" in captured.out
    assert "exit" in captured.out


def test_exit_sets_running_false(capsys):
    app = App()
    app.exit()
    assert app.running is False
    captured = capsys.readouterr()
    assert "Программа завершена" in captured.out


@pytest.mark.parametrize(
    "command,expected_output",
    [
        ("add 2 3", "Результат: 5"),
        ("sub 3 2", "Результат: 1"),
        ("mult 2 3", "Результат: 6"),
        ("div 4 2", "Результат: 2"),
    ],
)
def test_run_operations(mock_calc, command, expected_output, capsys):
    inputs = iter([command, "exit"])
    with patch.object(builtins, "input", lambda _: next(inputs)):
        app = App(calculator_cls=mock_calc)
        app.run()
        output = capsys.readouterr().out
        assert expected_output in output


def test_run_invalid_command(mock_calc, capsys):
    inputs = iter(["unknown", "exit"])
    with patch.object(builtins, "input", lambda _: next(inputs)):
        app = App(calculator_cls=mock_calc)
        app.run()
        output = capsys.readouterr().out
        assert '"unknown" такой команды нет' in output


def test_run_invalid_args(mock_calc, capsys):
    inputs = iter(["add 2 a", "exit"])
    with patch.object(builtins, "input", lambda _: next(inputs)):
        app = App(calculator_cls=mock_calc)
        app.run()
        output = capsys.readouterr().out
        assert "Ошибка: Аргументы должны быть числами" in output


def test_run_division_by_zero(mock_calc, capsys):
    mock_instance = mock_calc.return_value
    mock_instance.div.side_effect = ZeroDivisionError("деление на ноль")

    inputs = iter(["div 2 0", "exit"])
    with patch.object(builtins, "input", lambda _: next(inputs)):
        app = App(calculator_cls=mock_calc)
        app.run()
        output = capsys.readouterr().out
        assert "Ошибка: деление на ноль" in output