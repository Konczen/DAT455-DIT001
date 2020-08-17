# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *

def graphicInput(ggame):
    gplayer = ggame.getCurrentPlayer()
    oldAngle,oldVel = gplayer.getAim()
    wind = ggame.getCurrentWind()

    inp = InputDialog(oldAngle,oldVel,wind)

    if inp.interact() == "Fire!": 
        newAngle, newVel = inp.getValues()
        inp.close()
        return newAngle,newVel
        
    elif inp.interact() == "Quit":
        exit()


def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj


def graphicfinishShot(ggame, gproj):
    gPlayer = ggame.getCurrentPlayer()
    other = ggame.getOtherPlayer()
    distance = other.projectileDistance(gproj)

    if distance == 0.0:
        gPlayer.increaseScore()
        ggame.newRound()

    ggame.nextPlayer()

def graphicPlay():
    ggame = GraphicGame(Game(10,3))
    
    while True: 
        angle, vel = graphicInput(ggame)
        gproj = graphicFire(ggame,angle, vel)
        graphicfinishShot(ggame,gproj)

graphicPlay() 


