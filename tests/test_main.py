from unittest.mock import patch
import runpy

from praktikum.main import main


def test_main_calls_print():
    with patch('builtins.print') as mock_print:
        main()
    assert mock_print.called


def test_main_script_entry_point():
    with patch('builtins.print') as mock_print:
        runpy.run_module('praktikum.main', run_name='__main__')
    assert mock_print.called
