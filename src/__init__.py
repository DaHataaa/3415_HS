from gameserver import GameServer

def __main__():
    # Можно добавить обработчик параметров коммандной строки, например --load <file>
    server = GameServer()
    server.run()

if __name__ == "__main__":
    __main__()
