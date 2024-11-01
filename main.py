from ftp import FtpServer


def command_list():
    print('Список доступных комманд:')
    print('1. Создать каталог на сервере;')
    print('2. Удалить каталог на сервере;')
    print('0. Выход из программы.')


def main_menu(ftp_connection: FtpServer) -> None:
    command_list()

    while True:
        command = input('Выберите команду: ')
        if command == '1':
            dir_name = input('Введите имя создаваемого каталога: ')
            ftp_connection.make_directory(dir_name)
            command_list()

        elif command == '2':
            dir_name = input('Введите имя удаляемого каталога: ')
            ftp_connection.delete_directory(dir_name)
            command_list()

        elif command == '0':
            return None
        else:
            print('Введенная команда не существует')
            command_list()


if __name__ == '__main__':
    SERVER_ADDRESS = input("Введите ftp адресс: ")
    USERNAME = input("Введите логин: ")
    PASSWORD = input("Введите пароль: ")

    try:
        ftp = FtpServer(SERVER_ADDRESS, USERNAME, PASSWORD)
        main_menu(ftp)

        ftp.close()
    except Exception as e:
        print(f'Ошибка: {e}')
