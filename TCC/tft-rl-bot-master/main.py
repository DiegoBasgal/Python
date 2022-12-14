from controller import Controller
from screen import ScreenInterpreter
from state import GameState
from player import Player
from time import sleep

def testReader():
    sleep(1)
    gs = GameState(ScreenInterpreter(speed=0.2))
    player = Player(gs)
    while True:
        gs.update()
        print("Gold: ", gs.getGold())
        print("Level: ", gs.getLevel())
        print("Store: ", gs.getStore())
        print("xp: ", gs.getXpToLevelUp())
        print("Hp: ", gs.getHp())
        player.randomAction()
        sleep(0.1)

def testTrainer():
    c = Controller()
    print(c.pool)
    print(c.odds)
    shop = c.refreshShop([None, None, None, None, None], 1)
    for i in range(9):
        print(shop)
        shop = c.refreshShop(shop, i + 1)

if __name__ == '__main__':
    # testTrainer()
    testReader()
    # testPlayer()
