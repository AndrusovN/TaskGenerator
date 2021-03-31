import random


# Тупая генерация простого примера линейного уравнения
def generate_random():
    a = random.randint(1, 10)
    a1 = random.randint(2, 10)
    b = random.randint(1, 10)
    b1 = random.randint(2, 10)
    c = random.randint(-100, 100)
    c1 = random.randint(2, 10)
    text = '\\frac{' + str(a) + '}{' + str(a1) + '}x + ' + \
           '\\frac{' + str(b) + '}{' + str(b1) + '} = ' + \
           '\\frac{' + str(c) + '}{' + str(c1) + '}'
    return text


# Генерируем несколько примеров и оборачиваем в tex-формат (с document и все такое)
def generate_sample():
    result =  '''
\\title{Уравнения}

\\begin{document}
    \\maketitle

    Примеры:
    \\begin{itemize}
'''
    for i in range(5):
        result += '\t\t\\item $' + generate_random() + '$\n'
    result += '''
    \\end{itemize}
\\end{document}
'''

    return result
