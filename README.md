Проект " Игры разума":
В проекте представлены 5 логических игр:
1) Четное/нечетное (brain-even)
2) Калькулятор, вычисляющий примеры из двух переменных( используются операторы +,-,*) (brain-calc)
3) Наибольший общий делитель (brain-gcd)
4) Арифметическая прогрессия (поиск пропущенного звена) (brain-progression)
5) Простое ли число (brain-prime)

Игры имеют общую логику, и запускаются "движком" ( из модуля common_logic), получающим на вход игру.
Из игры извлекается 3 необходимые переменные (вопрос, правильный ответ и разные для каждой игры правила игры (константа RULE_OF_THE_GAME)
Далее, переменные подставляются в функцию общей логики и все игры происходят по общему сценарию:
1) Приветствие + получение имени игрока
2) вывод правил игры
3) игра вопрос-ответ, где игрок должен дать 3 верных ответа для победы
4) при ошибке выдается специальное сообщение и игра завершается. "Let's try again))", попробуй снова, предлагает программа. 






<a href="https://asciinema.org/a/BohA73gUA3UOK1amUXtpYGWxF" target="_blank"><img src="https://asciinema.org/a/BohA73gUA3UOK1amUXtpYGWxF.svg" /></a>
<a href="https://asciinema.org/a/79eHBuovbqd5fearkLFY037CX" target="_blank"><img src="https://asciinema.org/a/79eHBuovbqd5fearkLFY037CX.svg" /></a>
<a href="https://asciinema.org/a/0CoVMZFXJOS6b6Krl4hK3Lt5n" target="_blank"><img src="https://asciinema.org/a/0CoVMZFXJOS6b6Krl4hK3Lt5n.svg" /></a>
<a href="https://asciinema.org/a/26kvATgVZy2r2Q9oYf9LGEo9W" target="_blank"><img src="https://asciinema.org/a/26kvATgVZy2r2Q9oYf9LGEo9W.svg" /></a>
<a href="https://asciinema.org/a/nXcuPDg1zYC7iGwHNJZuW0Jeb" target="_blank"><img src="https://asciinema.org/a/nXcuPDg1zYC7iGwHNJZuW0Jeb.svg" /></a>
<script src="https://asciinema.org/a/14.js" id="asciicast-14" async data-autoplay="true" data-size="big"></script>

### Hexlet tests and linter status:
https://github.com/MarfaNikitina/python-project-lvl1/.github/workflows/main.yml/badge.svg)

[![linter check](https://github.com/MarfaNikitina/python-project-lvl1/actions/workflows/hexlet-lint.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl1/actions/workflows/hexlet-lint.yml)

[![Actions Status](https://github.com/MarfaNikitina/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl1/actions)
