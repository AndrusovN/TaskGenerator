# TaskGenerator
Простенький генератор задачек

## Установка
Вам понадобится
1. Python, добавленный в PATH (https://www.python.org/downloads/)
2. PDFLaTeX, добавленный в PATH (это можно сделать на двух основных сайтах: TexLive (много весит, но все и сразу) - http://tug.org/texlive/acquire-netinstall.html
или MikTex (весит мало, но придется немного покопаться с установкой доп модулей, хотя это не очень сложно, так как если открыть в идущем в коробке редакторе
[файлик преамбулы](tmp/empty.tex), то редактор сам предложит установить недостающие пакеты) - https://miktex.org/)

Когда это все установлено, можно просто скачать все файлы данного репозитория и использовать программу

## Использование
Можно просто запустить main.py, тогда программа создаст 5 случайных примеров линейных уравнений (результат будет обновлен и сохранится в [этот файл](examples/test.pdf)).
Также можно копаться в коде и менять самим какие-то параметры, чтобы получить желаемый результат.
