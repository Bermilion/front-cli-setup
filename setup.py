# -*- coding: utf-8 -*-

import os
import subprocess
import json

env = os.environ
downloader = 'curl' if os.path.exists('/usr/bin/curl') else 'wget'
directory = env['HOME'] + '/.front-cli'

if os.path.exists(directory):
    print ('Update')
    os.chdir(directory)
    os.system('git pull')
else:
    os.mkdir(directory)
    os.chdir(directory)
    print (os.getcwd())
    os.system('git clone https://github.com/Bermilion/front-cli.git ./')
    subprocess.call(['/usr/bin/pkexec', 'ln', '-s', directory + '/cli.py', '/usr/local/bin'])
    os.mkdir(directory + '/presets')
    os.chdir(env['HOME'])
    with open('.bashrc', 'a') as file:
        file.write('alias front="python /usr/local/bin/cli.py"\n')

def installExtentions ():
    os.system('pip install click')
    try:
        os.system('pip install mysqlclient')
    except:
        subprocess.call(['/usr/bin/pkexec', 'apt', 'install', 'python-dev', 'default-libmysqlclient-dev'])
        try:
            os.system('pip install mysqlclient')
        except:
            print ('Это какая то супер ошибка')

if os.path.exists('/usr/local/bin/pip'):
    installExtentions()
else:
    if downloader == 'curl':
        os.system(downloader + ' https://bootstrap.pypa.io/get-pip.py -o get-pip.py | python')
    else:
        os.system(downloader + ' https://bootstrap.pypa.io/get-pip.py -O get-pip.py | python')

    os.system('pip install -U pip')
    installExtentions()

# Настройка конфигурации
os.chdir(directory)
with open('conf.json', 'w') as file:
    pass
print ('Конфигурациооный файл создан')

print('Настройка файла конфигурации')
print ('Автаризационные данные mySQL\n')

user = 'root'
password = '0000'

def sqlData(login, password):
    with open('conf.json', 'a') as file:
        data = {
            "mysql": {
                "user": login,
                "password": password
            }
        }
        json.dump(data, file, sort_keys=True, indent=4)

choiceMySQLAuth = raw_input('По умолчанию user: root, password: 0000 [Да/нет]:')
if len(choiceMySQLAuth) == 0 or choiceMySQLAuth == 'да' or choiceMySQLAuth == 'Да' or choiceMySQLAuth == 'Д' or choiceMySQLAuth == 'y' or choiceMySQLAuth == 'Y' or choiceMySQLAuth == 'yes' or choiceMySQLAuth == 'Yes':
    print ('Применины настройки по умолчанию')
else:
    user = raw_input('Логин: ')
    password = raw_input('Пароль: ')
    print (user, password)

sqlData(user, password)


# настройка корневой директории
defaultRootDir = env['HOME'] + '/sites'
rootDir = raw_input('\nУказать корневую директорию для проектов?\n\n0 — не создаст корневой директории.\n1 — ' + defaultRootDir + '\nИли введите свой вариант (необходимо ввести полный путь):')

def createRootDirKey(dir):
    os.chdir(directory)

    with open('conf.json', 'r') as file:
        data = json.load(file)
        data['root-dir'] = dir

        with open('conf.json', 'w') as file:
            json.dump(data, file, sort_keys=True, indent=4)

def dirExists(path):
    if os.path.exists(path):
        createRootDirKey(path)
    else:
        os.mkdir(path)
        createRootDirKey(path)

if rootDir == '0':
    print ('Инициализация будет происходить относительно текущего терминального пути.')
elif rootDir == '1':
    dirExists(defaultRootDir)
else:
    dirExists(rootDir)