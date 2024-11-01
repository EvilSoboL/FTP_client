from ftp import FtpServer

'''
fpm2.ami.nstu.ru
pmi-m6307
NP%1pFP6G
'''

if __name__ == '__main__':
    server_address = input("Введите ftp адресс: ")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    try:
        ftp = FtpServer(server_address, username, password)
        ftp.close()
    except Exception as e:
        print('Неудалось подключится к серверу')
