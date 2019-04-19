# -*- coding: utf-8 -*-

import os
import subprocess

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

if os.path.exists('/usr/local/bin/pip'):
    installExtentions()
else:
    if downloader == 'curl':
        os.system(downloader + ' https://bootstrap.pypa.io/get-pip.py -o get-pip.py | python')
    else:
        os.system(downloader + ' https://bootstrap.pypa.io/get-pip.py -O get-pip.py | python')

    os.system('pip install -U pip')
    installExtentions()

