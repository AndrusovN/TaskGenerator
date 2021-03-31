from generator import generate_sample
from maker import make

# Тут стандартные настройки, можете заменить на то, что в комментариях или написать свой ввод данных о файле
# Например, по идее надо через диалоговое окно делать
directory = 'examples'  # input('Введите директорию, в которую хотите сохранить пример\n')
filename = 'test'  # input('Введите имя файла\n')

# Генерируем текст примера
text = generate_sample()

# Создаем pdf-ку, logs - это, собственно, логи pdflatex, которые могут быть интересны
make(text, directory, filename)
print('Завершено')
