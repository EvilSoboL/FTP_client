from ftp import FtpServer


def command_list():
    print('Список доступных комманд:')
    print('1. Создать каталог на сервере')
    print('2. Удалить каталог на сервере')
    print('3. Вывести содержимое каталога')
    print('4. Сменить каталог')
    print('5. Получить файл')
    print('6. Загрузить файл ')
    print('7. Переименовать файл')
    print('0. Выход из программы')


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

        elif command == '3':
            ftp_connection.show_directory_contents()
            command_list()

        elif command == '4':
            dir_name = input('Введите имя каталога, в который хотите переместиться: ')
            ftp_connection.change_directory(dir_name)

        elif command == '5':
            filename = input('Введите имя файла, который хотите получить: ')
            local_filename = input('Введите имя для сохраненного файла: ')
            ftp_connection.download_file(filename, local_filename)

        elif command == '6':
            filename = input('Введите имя файла, который хотите загрузить: ')
            local_filename = input('Введите имя для загружаемого файла: ')
            ftp_connection.upload_file(filename, local_filename)

        elif command == '7':
            filename = input('Введите имя файла, который хотите переименовать: ')
            new_filename = input('Введите новое имя для файла: ')
            ftp_connection.rename_file(filename, new_filename)

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
