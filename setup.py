# -*- coding: utf-8 -*-

import os
import subprocess
import json

env = os.environ
downloader = 'curl' if os.path.exists('/usr/bin/curl') else 'wget'
directory = env['HOME'] + '/.front-cli'

def confSQL():
    os.chdir(directory)
    with open('conf.json', 'w') as file:
        pass
    print ('Конфигурациооный файл создан')

    # subprocess.call(['touch', 'conf.json'])
    print('Настройка файла конфигурации')
    print ('\nАвтаризационные данные mySQL \nпо умолчанию login: root, password: 0000\n')

    login = 'root'
    password = '0000'

    def sqlData(login, password):
        with open('conf.json', 'a') as file:
            mySqlData = {
                "mysql": {
                    "login": login,
                    "password": password
                }
            }
            json.dump(mySqlData, file, sort_keys=True, indent=4)

    choiceMySQLAuth = raw_input('[Да/нет]:')
    if len(
            choiceMySQLAuth) == 0 or choiceMySQLAuth == 'да' or choiceMySQLAuth == 'Да' or choiceMySQLAuth == 'Д' or choiceMySQLAuth == 'y' or choiceMySQLAuth == 'Y' or choiceMySQLAuth == 'yes' or choiceMySQLAuth == 'Yes':
        print ('По умолчанию')
    else:
        login = raw_input('Логин: ')
        password = raw_input('Пароль: ')
        print (login, password)

    sqlData(login, password)

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
    os.chdir(env['HOME'])
    with open('.bashrc', 'a') as file:
        file.write('alias front="python /usr/local/bin/cli.py"\n')

    os.chdir(directory)
    subprocess.call(['touch', 'conf'])
    print('Настройка файла конфигурации')
    with open('conf', 'a') as file:
        file.write('[mysql]\n')

def installExtentions ():
    os.system('pip install click')
    confSQL()

if os.path.exists('/usr/local/bin/pip'):
    installExtentions()
else:
    if downloader == 'curl':
        os.system(downloader + ' https://bootstrap.pypa.io/get-pip.py -o get-pip.py | python')
    else:
        os.system(downloader + ' https://bootstrap.pypa.io/get-pip.py -O get-pip.py | python')

    os.system('pip install -U pip')
    installExtentions()

