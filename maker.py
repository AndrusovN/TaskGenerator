import os
from shutil import copyfile
# Где лежит файлик с преамбулой
TEMPLATE_FILE = 'tmp\\empty.tex'


# Основная функция создания файла
def make(text, directory, filename):
    # Читаем преамбулу
    template_file = open(TEMPLATE_FILE, 'r')
    template = '\n'.join(template_file.readlines())
    template_file.close()

    # Переносим преамбулу в основной файл (сохраняем его в tmp\)
    temporary_name = 'tmp\\' + filename
    temporary_output = open(temporary_name + '.tex', 'w', encoding='utf-8')
    temporary_output.write(template)
    # Вписываем туда же основной текст файла
    temporary_output.write(text)
    temporary_output.close()

    # Переходим в папку tmp, чтобы вызвать там pdflatex
    cur_dir = os.path.abspath('.')
    os.chdir(cur_dir + '\\tmp')
    # Запускаем pdflatex, получаем pdf
    os.system('pdflatex ' + filename + '.tex')

    # Возвращаемся
    os.chdir(cur_dir)

    # Копируем файл в нужную директорию
    copyfile(temporary_name + '.pdf', directory + '\\' + filename + '.pdf')

    # Чистим tmp\
    os.remove(temporary_name + '.tex')
    os.remove(temporary_name + '.log')
    os.remove(temporary_name + '.aux')
    os.remove(temporary_name + '.out')
    os.remove(temporary_name + '.pdf')
