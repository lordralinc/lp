import platform, time, os, re, json
from os import environ
s = platform.python_version()
print("Mодуль написал Люцифер Денница")
time.sleep(2)
print("Определяю версию питона")
time.sleep(2)
a = s.rpartition('.')[0]
python = f"python{a}"
print(python)
print("Работает на питоне 3.7, 3.8, 3.9")
time.sleep(2)
print("Определяю систему")
time.sleep(2)
sis = os.name
print("""
Что ты используешь?
1 -> Termux
2 -> Linux
""")
l = input('Напиши цифру правильного варианта')

if str(l) == '1':
    print("Блять, ебаный термукс, как же я тебя нахуй ненавижу")
    time.sleep(2)
    diiirict = os.getcwd()
    print(f'Текущая директория: {diiirict}')
    time.sleep(2)
    dirict_rab = re.sub(r'/lp', '', diiirict).strip()
    os.chdir(str(dirict_rab))
    ddd = os.getcwd()
    print(f'Рабочая дириктория: {ddd}')
    time.sleep(2)
    print(f"Создаю лп в дириктории {ddd}")
    os.system("git clone https://github.com/lordralinc/idm_lp.git")
    dir_lp = f'{ddd}/idm_lp'
    os.chdir(str(dir_lp))
    time.sleep(2)
    print("Устанавливаю модули")
    time.sleep(2)
    os.system(f'env/bin/{python} -m pip install -r requirements.txt')
    os.system(f'{python} -m pip install requests')
    import requests

    login = input("Введите логин от вк: ")
    password = input("Введите пароль от вк: ")
    secret_code = input("Введите секретный код от идм: ")
    try:
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token = str(get_token.json()["access_token"])
        print("Получил первый токен")
        time.sleep(5)
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token2 = str(get_token.json()["access_token"])
        print("Получил второй токен")
        time.sleep(5)
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token3 = str(get_token.json()["access_token"])
        print("Получил третий токен")
    except:
        print("Не удалось получить токен\nПроверьте логин и пароль")
        exit()

    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] = [token]
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] += [token2]
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] += [token3]
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    print('Вставил токены в конфиг')
    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['secret_code'] = secret_code
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    print("Установил секретный код")
    if str(python) == "python3.9":
        os.system(f'{python} -m pip uninstall loguru')
        print(
            f"Для запуска тебе надо прописать:\ncd {dir_lp}\nnohup env/bin/{python} main.py &\nОбязательно запомни номер процесса что бы потом остановить\nОстанавливать скрипт надо командой kill (Номер процесса без скобок)\nТак же пропиши команду: rm -r nohup.out для стабильной работы")

    print(
        f"Для запуска тебе надо прописать:\ncd {dir_lp}\nnohup env/bin/{python} main.py &\nОбязательно запомни номер процесса что бы потом остановить\nОстанавливать скрипт надо командой kill (Номер процесса без скобок)\nТак же пропиши команду: rm -r nohup.out для стабильной работы")

elif str(l) == '2':
    print("Ну с линуксом ща намутим")
    time.sleep(2)
    diiirict = os.getcwd()
    print(f'Текущая директория: {diiirict}')
    time.sleep(2)
    dirict_rab = re.sub(r'/lp', '', diiirict).strip()
    os.chdir(str(dirict_rab))
    ddd = os.getcwd()
    print(f'Рабочая дириктория: {ddd}')
    time.sleep(2)
    print(f"Создаю лп в дириктории {ddd}")
    os.system("git clone https://github.com/lordralinc/idm_lp.git")
    dir_lp = f'{ddd}/idm_lp'
    os.chdir(str(dir_lp))
    time.sleep(2)
    print("Создаю виртуальное окружение")
    os.system(f'{python} -m venv env')
    print("Устанавливаю модули")
    time.sleep(2)
    os.system(f'env/bin/{python} -m pip install -r requirements.txt')
    os.system(f'{python} -m pip install requests')
    import requests
    login = input("Введите логин от вк: ")
    password = input("Введите пароль от вк: ")
    secret_code = input("Введите секретный код от идм: ")
    try:
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token = str(get_token.json()["access_token"])
        print("Получил первый токен")
        time.sleep(5)
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token2 = str(get_token.json()["access_token"])
        print("Получил второй токен")
        time.sleep(5)
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token3 = str(get_token.json()["access_token"])
        print("Получил третий токен")
    except:
        print("Не удалось получить токен\nПроверьте логин и пароль")
        exit()

    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] = [token]
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] += [token2]
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] += [token3]
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    print('Вставил токены в конфиг')
    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['secret_code'] = secret_code
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=True, indent=2))
    print("Установил секретный код")
    if str(python) == "python3.9":
        os.system(f'{python} -m pip uninstall loguru')
        print(f"Для запуска тебе надо прописать:\ncd {dir_lp}\nnohup env/bin/{python} main.py &\nОбязательно запомни номер процесса что бы потом остановить\nОстанавливать скрипт надо командой kill (Номер процесса без скобок)\nТак же пропиши команду: rm -r nohup.out для стабильной работы")

    print(f"Для запуска тебе надо прописать:\ncd {dir_lp}\nnohup env/bin/{python} main.py &\nОбязательно запомни номер процесса что бы потом остановить\nОстанавливать скрипт надо командой kill (Номер процесса без скобок)\nТак же пропиши команду: rm -r nohup.out для стабильной работы")



