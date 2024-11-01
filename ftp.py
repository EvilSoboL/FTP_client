from ftplib import FTP
import socket


class FtpServer:
    def __init__(self, ftp_address: str, username: str, password: str):
        self.ftp_address = ftp_address
        self.username = username
        self.password = password

        self.connection = self.connect()

    def connect(self) -> FTP | None:
        try:
            ftp = FTP(timeout=10)
            ftp.connect(self.ftp_address)

            ftp.login(user=self.username, passwd=self.password)
            print('Соединение установлено')
            return ftp

        except socket.gaierror:
            print(f'Ошибка: Невозможно разрешить адрес {self.ftp_address}')

        except socket.error as e:
            print(f'Ошибка сокета: {e}')

        except ConnectionRefusedError:
            print(f'Подключение к {self.ftp_address} отклонено')

        except TimeoutError:
            print(f'Превышено время ожидания при подключении к {self.ftp_address}')

        except Exception as e:
            print(f'Ошибка при подключении: {e}')

        return None

    def make_directory(self, directory_name: str) -> None:
        self.connection.mkd(directory_name)
        print(f'Каталог {directory_name} успешно создан')

    def delete_directory(self, directory_name: str) -> None:
        self.connection.rmd(directory_name)
        print(f'Каталог {directory_name} успешно удален')

    def show_directory_contents(self) -> None:
        print(self.connection.dir('.'))

    def close(self):
        self.connection.close()
        print('Соединение разорвано')
