from math import sin,cos,radians
import random

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        p1 = Player("blue",-90, self, 40, 45)
        p2 = Player("red", 90, self, 40, 45)
        self.players = [p1,p2]
        self.CurrentPlayerNumber = 0
        self.Wind = random.randint(-10, 11)

    """ A list containing both players """
    def getPlayers(self):
        return self.players 

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannonSize 

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ballSize 

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.players[self.getCurrentPlayerNumber()] 

    """ The opponent of the current player """
    def getOtherPlayer(self):
        if self.getCurrentPlayerNumber() == 0:
            return self.players[1]
        elif self.getCurrentPlayerNumber() == 1:
            return self.players[0] 
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.CurrentPlayerNumber 
    
    """ Switch active player """
    def nextPlayer(self):
        if self.getCurrentPlayerNumber() == 0:
            self.CurrentPlayerNumber = 1
        else:
            self.CurrentPlayerNumber = 0 

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
       self.Wind = wind

    
    def getCurrentWind(self):    
        return self.Wind


    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.Wind = random.randint(-10, 11)
        self.CurrentPlayerNumber = 0


""" Models a player """
class Player:

    def __init__ (self, color, Xaxis, game, angle, velocity):
        self.color = color
        self.Xaxis = Xaxis
        self.game = game
        self.angle = angle
        self.velocity = velocity 
        self.currentScore = 0
    
    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        self.angle = angle
        self.velocity = velocity
        if self.game.getCurrentPlayerNumber() == 1:
            angle=180-angle

        proj = Projectile(angle, velocity, self.game.getCurrentWind(), self.getX(), self.game.getCannonSize()/2, -110, 110)
        
        return proj 

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        cannonMid = self.getX()
        cannonSize = self.game.getCannonSize()/2

        cannonLeft = cannonMid - cannonSize
        cannonRight = cannonMid + cannonSize

        projectileMid = proj.getX()
        projectileSize = self.game.getBallSize()
        
        projectileLeft = projectileMid - projectileSize
        projectileRight = projectileMid + projectileSize

        if projectileLeft > cannonRight:
            return -cannonRight + projectileLeft
        elif projectileRight < cannonLeft:
            return -cannonLeft + projectileRight
        else:
            return 0

    """ The current score of this player """
    def getScore(self):
        return self.currentScore 

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.currentScore += 1 

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.Xaxis 

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.angle, self.velocity 



""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
