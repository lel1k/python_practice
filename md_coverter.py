# title Markdown converter
# description Конвертирует код из .py файла в файл формата .md с добавлением оглавления, названия задачи и её краткого описания


# ---end----
from os.path import exists

def md_converter(file,project):

    project_exists = exists(project)



    with open(file, 'r') as content:
        content = content.readlines()


    if project_exists:
        with open(project, 'r') as data:
            data = data.readlines()

    else:
        data = []

    new_data = open(project,'w')


    was_code_started = False

    if not project_exists:

        data.append('# {}\n'.format(project[:-3]))

        data.append('<!--content-->\n')

    for string in content:

        if was_code_started:
            data.append(string)

        if string.startswith('# title'):
            title = string[8:-1]
            data.append('## {}\n'.format(string[7:]))
        if string.startswith('# description'):
            data.append('{}\n'.format(string[len('# description'):]))




        if string.startswith('# ---end----'):
            data.append('```pyton\n')
            was_code_started = True

    data.append('```\n')


    index = data.index('<!--content-->\n')

    data.insert(index,'+ [{}](#{})'.format(title,"-".join(title.lower().split())) + '\n')

    for el in data:
        new_data.write(el)

md_converter('md_coverter.py','project.md')