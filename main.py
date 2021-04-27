import json
import os
import sys
import time
from enum import Enum
from typing import Tuple

try:
    import requests
except ImportError:
    import pip
    print("Installing requests")

    pip.main(['install', "requests"])
    import requests


class LPSetupException(Exception):

    def __init__(self, code: int, desc: str, sys_code: int = 0):
        self.code = code
        self.description = desc
        self.system_exit_code = sys_code

    def __repr__(self) -> str:
        return f"LPSetupException(code={self.code}, description={self.description})"

    def __str__(self) -> str:
        return f"[{self.code}] {self.description}"

    @classmethod
    def invalid_python(cls):
        return cls(0, "Не верная версия python. Только 3.6+")

    @classmethod
    def invalid_system(cls):
        return cls(1, "Вы отменили установку")

    @classmethod
    def invalid_vk(cls):
        return cls(2, "Не верный логин или пароль")

    @classmethod
    def error_vk(cls, description: str):
        return cls(3, f"Ошибка ВК: {description}")

    @classmethod
    def cancel(cls):
        return cls(4, "Вы отменили установку")


class SystemEnum(Enum):
    TERMUX = 1
    LINUX = 2


def system_call(command: str):
    print(command)
    os.system(command)


def screen_clear():
    print('=' * 10, '\n' * 50)


def get_python() -> str:
    if sys.version_info.major != 3:
        raise LPSetupException.invalid_python()
    if sys.version_info.minor < 6:
        raise LPSetupException.invalid_python()
    return sys.executable


def get_directories() -> Tuple[str, str]:
    parent_directory = os.path.dirname(os.path.dirname(__file__))
    lp_directory = os.path.join(parent_directory, "idm_lp")
    return os.path.abspath(parent_directory), os.path.abspath(lp_directory)


def git_clone(parent_directory: str, working_directory: str):
    print(f"Загружаю файлы в {working_directory}")
    os.chdir(parent_directory)
    system_call("git clone https://github.com/lordralinc/idm_lp.git")
    os.chdir(working_directory)
    print("Файлы загружены")


def get_venv_python(main_python: str, working_directory: str, system_info: SystemEnum) -> str:
    if system_info == system_info.TERMUX:
        return main_python
    system_call(f'{main_python} -m venv env')
    return os.path.join(working_directory, 'env', 'bin', f'python{sys.version_info.major}.{sys.version_info.minor}')


def install_pip(python_cmd: str):
    print(f"Устанавливаю модули")
    system_call(f'{python_cmd} -m pip install -r requirements.txt')
    system_call(f'{python_cmd} -m pip install requests')
    if sys.version_info.major == 3 and sys.version_info.minor == 9:
        os.system(f'{python_cmd} -m pip uninstall loguru')
    print(f"Модули установлены")


def get_access_token(login: str, password: str, code: str = None) -> str:
    url = (
        f"https://oauth.vk.com/token?grant_type=password&client_id=2274003&"
        f"client_secret=hHbZxrka2uZ6jB1inYsH&username={login}&password={password}&2fa_supported=1"
    )
    if code:
        url += "&code=" + code
    request = requests.get(url).json()

    if 'error' in request:
        if 'error_type' in request:
            if request['error_type'] == 'username_or_password_is_incorrect':
                raise LPSetupException.invalid_vk()
        if request['error'] == 'need_validation':
            code = input(f"Введите код подтверждения VK:\n{request['redirect_uri']}")
            return get_access_token(login, password, code)
        raise LPSetupException.error_vk(request['error'])

    return request['access_token']


def main():
    python_cmd = get_python()
    print(f"Скрипт написал Люцифер «Ебаный Пидарас» Денница\n")

    system = input(
        "Выберите систему:\n"
        "    1. Termux\n"
        "    2. Linux\n"
        "[1,2]> "
    )
    screen_clear()
    if system not in ('1', '2',):
        raise LPSetupException.invalid_system()

    system = SystemEnum(int(system))
    print(f"Будет использован интерпритатор: {python_cmd}\n")

    parent_directory, working_directory = get_directories()
    print(f"Родительская директория: {parent_directory}")
    print(f"Рабочая директория: {working_directory}\n")
    print(f"Устанавливаеим под {system.name}\n")

    if input("Все правильно? [y/n]> ").lower() not in ("y", "д", "yes", "да", "+"):
        raise LPSetupException.cancel()

    screen_clear()
    git_clone(parent_directory, working_directory)
    venv_python = get_venv_python(python_cmd, working_directory, system)
    install_pip(venv_python)

    login = input("Введите логин от VK: ")
    password = input("Введите пароль от VK: ")
    secret_code = input("Введите секретный код от IDM: ")

    tokens = []
    while len(tokens) != 3:
        time.sleep(1)
        try:
            access_token = get_access_token(login, password)
        except LPSetupException as expt:
            if expt.code == 2:
                print(expt)
                login = input("Введите логин от VK: ")
                password = input("Введите пароль от VK: ")
            else:
                raise expt
        else:
            if access_token is None:
                continue
            tokens.append(access_token)

    with open('config.json', 'r', encoding='utf-8') as f:
        config_file = json.loads(f.read())
    config_file['tokens'] = tokens
    config_file['secret_code'] = secret_code
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(config_file, ensure_ascii=False, indent=2))

    print("Установил секретный код\n\n\n")
    print(
        f"Для запуска тебе надо прописать:\n"
        f"cd {working_directory}\n"
        f"nohup {venv_python} main.py &\n"
        f"Обязательно запомни номер процесса что бы потом остановить\n"
        f"Останавливать скрипт надо командой kill (Номер процесса без скобок)\n"
        f"Так же пропиши команду: rm -r nohup.out для стабильной работы"
    )


if __name__ == "__main__":
    try:
        main()
    except LPSetupException as ex:
        print("Произошла ошибка при установке:\n", ex)
        exit(ex.system_exit_code)
    except Exception as ex:
        print("Произошла неизвестная ошибка при установке:\n", ex)
        exit(1)
