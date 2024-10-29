from os import system

def imports():
    while True:
        try:
            import json
            import pygame
            import enum
            break
        except Exception:
            system('''pip install json pygame enum''')

