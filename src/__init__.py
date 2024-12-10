from src import gameserver

def __main__():
    # Можно добавить обработчик параметров коммандной строки, например --load <file>
    server = gameserver.GameServer()
    server.run()

if __name__ == "__main__":
    __main__()
