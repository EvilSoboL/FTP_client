from ftp import FtpServer


def command_list(ftp_connection: FtpServer) -> None:
    print('Список доступных комманд:')
    print('1. Создать каталог на сервере;')
    print('0. Выход из программы.')

    while True:
        command = input('Выберите команду: ')
        if command == '1':
            dir_name = input('Введите имя создаваемого каталога: ')
            ftp_connection.make_directory(dir_name)
        elif command == '0':
            return None
        else:
            print('Введенная команда не существует')


if __name__ == '__main__':
    SERVER_ADDRESS = input("Введите ftp адресс: ")
    USERNAME = input("Введите логин: ")
    PASSWORD = input("Введите пароль: ")

    try:
        ftp = FtpServer(SERVER_ADDRESS, USERNAME, PASSWORD)
        command_list(ftp)

        ftp.close()
    except Exception as e:
        print(f'Ошибка: {e}')
