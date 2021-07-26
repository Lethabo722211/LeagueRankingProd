
from main import get_league_log, init, get_input_data


def test_get_league_log():
    league_log = get_league_log('input.txt')
    assert league_log == {'Lions': 0, 'Snakes': 0, 'Tarantulas': 0, 'FC Awesome': 0, 'Grouches': 0}


def test_init(capsys):
    init('input.txt')
    printed = capsys.readouterr()
    assert printed.out == "1. Tarantulas, 6 pts\n" \
                          "2. Lions, 5 pts\n" \
                          "3. FC Awesome, 1 pts\n" \
                          "4. Snakes, 1 pts\n" \
                          "5. Grouches, 0 pts\n"


def test_get_input_data(monkeypatch, capsys):

    monkeypatch.setattr('builtins.input', lambda x: 'input.txt')
    get_input_data()
    printed = capsys.readouterr()
    assert printed.out == "1. Tarantulas, 6 pts\n" \
                          "2. Lions, 5 pts\n" \
                          "3. FC Awesome, 1 pts\n" \
                          "4. Snakes, 1 pts\n" \
                          "5. Grouches, 0 pts\n"
