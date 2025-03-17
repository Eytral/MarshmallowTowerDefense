import pygame
from Game.game import Game
import cProfile

# Creates and runs game object
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    cProfile.run("main()", sort="cumtime")