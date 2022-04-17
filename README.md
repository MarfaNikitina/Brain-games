Проект " Игры разума":
В проекте представлены 5 логических игр:
1) Четное/нечетное (brain-even)
2) Калькулятор, вычисляющий примеры из двух переменных( используются операторы +,-,*) (brain-calc)
3) Наибольший общий делитель (brain-gcd)
4) Арифметическая прогрессия (поиск пропущенного звена) (brain-progression)
5) Простое ли число (brain-prime)

Игры имеют общую логику, и запускаются "движком" ( из модуля common_logic), получающим на вход игру.
Из игры извлекается 3 необходимые переменные (вопрос, правильный ответ и разные для каждой игры правила игры (константа RULE)
Далее, переменные подставляются в функцию общей логики и все игры происходят по общему сценарию:
1) Приветствие + получение имени игрока
2) вывод правил игры
3) игра вопрос-ответ, где игрок должен дать 3 верных ответа для победы
4) при ошибке выдается специальное сообщение и игра завершается. "Let's try again))", попробуй снова, предлагает программа. 

[![asciicast](https://asciinema.org/a/BohA73gUA3UOK1amUXtpYGWxF.svg)](https://asciinema.org/a/BohA73gUA3UOK1amUXtpYGWxF)
[![asciicast](https://asciinema.org/a/79eHBuovbqd5fearkLFY037CX.svg)](https://asciinema.org/a/79eHBuovbqd5fearkLFY037CX)
[![asciicast](https://asciinema.org/a/0CoVMZFXJOS6b6Krl4hK3Lt5n.svg)](https://asciinema.org/a/0CoVMZFXJOS6b6Krl4hK3Lt5n)
[![asciicast](https://asciinema.org/a/26kvATgVZy2r2Q9oYf9LGEo9W.svg)](https://asciinema.org/a/26kvATgVZy2r2Q9oYf9LGEo9W)
[![asciicast](https://asciinema.org/a/nXcuPDg1zYC7iGwHNJZuW0Jeb.svg)](https://asciinema.org/a/nXcuPDg1zYC7iGwHNJZuW0Jeb)


### Hexlet tests and linter status:

<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/2c15c08d6adfe1e350ae/maintainability" /></a>

[![linter check](https://github.com/MarfaNikitina/python-project-lvl1/actions/workflows/hexlet-lint.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl1/actions/workflows/hexlet-lint.yml)

[![Actions Status](https://github.com/MarfaNikitina/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl1/actions)
