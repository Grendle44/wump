# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================
from types import MethodType
from Agent import Agent

class MyAI ( Agent ):

    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        
        # Agent's position
        Agent.x = 0
        Agent.y = 0

        # Agent's direction, start facing left as 1
        Agent.Dir = 1

        # Create 7x7 array to keep map
        Agent.Map = [[0 for i in range(7)] for i in range(7)]

		# Create 7x7 array to keep explored
        Agent.XMap = [[0 for i in range(7)] for i in range(7)]
        Agent.XMap[0][0] = True

        # Map for pits
        # Agent.PMap = [[0 for i in range(7)] for i in range(7)]

        # Map for wumpus
		# Agent.WMap = [[0 for i in range(7)] for i in range(7)]

        # The agent's next tile
        Agent.next = Agent.getNext()

        # Wumpus alive or not
        Agent.WumpAlive = True

        # Used Arrow or not
        Agent.Arrow = True 

        # Got the gold?
        Agent.GotGold = False

        # Track Cost
        Agent.Cost = 0

        # Agent has.Moved or not
        Agent.Moved = False

        pass
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================

        Agent.Cost += 1

        # 
        if Agent.x == 0 and Agent.y == 0:
        	if breeze and Agent.WumpAlive and not Agent.Arrow:
        		if Agent.Cost > 1:
        			return Agent.Action.CLIMB
        		return Agent.turnLeft()

       	# End condition when tired
        if Agent.Cost > 40 and Agent.x == 0 and Agent.y == 0:
        	return Agent.Action.CLIMB

        # Update next tile
        Agent.next = Agent.getNext()

        if not breeze and not stench:
        	Agent.Map[Agent.x][Agent.y] = 'X'

        if breeze and Agent.Moved:
        	Agent.Map[Agent.x][Agent.y] = 'B'
        	Agent.markPit()

        if scream:
        	Agent.WumpAlive = False


        if Agent.WumpAlive:
        	if stench and Agent.Moved:
        		# Mark stench
        		Agent.Map[Agent.x][Agent.y] = 'S'
        		# Mark all possible wumpus
        		Agent.markWump()
        		Agent.Moved = False
        		
        		# Todo: clear path
        		if Agent.Arrow:
        			return Agent.Action.SHOOT
	
        # If found gold
        if glitter:
        	Agent.Moved = False
        	Agent.GotGold = True
        	return Agent.Action.GRAB

        if bump:
        	# Mark wall
        	Agent.markWall()
        	# Corrent agent's position
        	if Agent.Dir == 0:
        		Agent.y -= 1
        	if Agent.Dir == 1:
        		Agent.x -= 1
        	if Agent.Dir == 2:
        		Agent.y += 1
        	if Agent.Dir == 3:
        		Agent.x += 1

        	return Agent.turnLeft()

        if Agent.GotGold and Agent.x == 0 and Agent.y == 0:
        	return Agent.Action.CLIMB

        # If hit wall
        # if Agent.x == 0:

        # If move forward
        if Agent.getNext() == 'pP' or Agent.getNext() == 'B' or Agent.getNext() == 'pW' or Agent.getNext() == 'S':
        	return Agent.turnLeft()

        return Agent.moveFow()
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

# Return agent's next tile in map
def getNext( self ):
	if Agent.Dir == 0:
		return Agent.Map[Agent.x][Agent.y + 1]
	if Agent.Dir == 1:
		return Agent.Map[Agent.x + 1][Agent.y]
	if Agent.Dir == 2:
		return Agent.Map[Agent.x][Agent.y - 1]
	if Agent.Dir == 3:
		return Agent.Map[Agent.x - 1][Agent.y]

# Mark possible pits locations
def markPit( self ):
	if Agent.Dir == 0:
		if Agent.Map[Agent.x + 1][Agent.y] != 'X': 
			Agent.Map[Agent.x + 1][Agent.y] = 'pP'
		if Agent.Map[Agent.x - 1][Agent.y] != 'X':
			Agent.Map[Agent.x - 1][Agent.y] = 'pP'
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pP'
	if Agent.Dir == 1:
		if Agent.Map[Agent.x + 1][Agent.y] != 'X':
			Agent.Map[Agent.x + 1][Agent.y] = 'pP'
		if Agent.Map[Agent.x][Agent.y - 1] != 'X':
			Agent.Map[Agent.x][Agent.y - 1] = 'pP'
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pP'
	if Agent.Dir == 2:
		# Agent v
		if Agent.Map[Agent.x + 1][Agent.y] != 'X':
			Agent.Map[Agent.x + 1][Agent.y] = 'pP'
		if Agent.Map[Agent.x - 1][Agent.y] != 'X':
			Agent.Map[Agent.x - 1][Agent.y] = 'pP'
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pP'
	if Agent.Dir == 3:
		# Agent <-
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pP'
		if Agent.Map[Agent.x - 1][Agent.y] != 'X':
			Agent.Map[Agent.x - 1][Agent.y] = 'pP'
		if Agent.Map[Agent.x][Agent.y - 1] != 'X':
			Agent.Map[Agent.x][Agent.y - 1] = 'pP'

# Mark possible wumpus locations
def markWump( self ):
	if Agent.Dir == 0:
		# Agent ^
		if Agent.Map[Agent.x + 1][Agent.y] != 'X':
			Agent.Map[Agent.x + 1][Agent.y] = 'pW'
		if Agent.Map[Agent.x - 1][Agent.y] != 'X':
			Agent.Map[Agent.x - 1][Agent.y] = 'pW'
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pW'
	if Agent.Dir == 1:
		# Agent ->
		if Agent.Map[Agent.x + 1][Agent.y] != 'X':
			Agent.Map[Agent.x + 1][Agent.y] = 'pW'
		if Agent.Map[Agent.x][Agent.y - 1] != 'X':
			Agent.Map[Agent.x][Agent.y - 1] = 'pW'
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pW'
	if Agent.Dir == 2:
		# Agent v
		if Agent.Map[Agent.x + 1][Agent.y] != 'X':
			Agent.Map[Agent.x + 1][Agent.y] = 'pW'
		if Agent.Map[Agent.x - 1][Agent.y] != 'X':
			Agent.Map[Agent.x - 1][Agent.y] = 'pW'
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pW'
	if Agent.Dir == 3:
		# Agent <-
		if Agent.Map[Agent.x][Agent.y + 1] != 'X':
			Agent.Map[Agent.x][Agent.y + 1] = 'pW'
		if Agent.Map[Agent.x - 1][Agent.y] != 'X':
			Agent.Map[Agent.x - 1][Agent.y] = 'pW'
		if Agent.Map[Agent.x][Agent.y - 1] != 'X':
			Agent.Map[Agent.x][Agent.y - 1] = 'pW'

# Move agent to the next tile
def moveFow( self ):
	if Agent.Dir == 0:
		Agent.y += 1
	if Agent.Dir == 1:
		Agent.x += 1
	if Agent.Dir == 2:
		Agent.y -= 1
	if Agent.Dir == 3:
		Agent.x -= 1

	Agent.Moved = True
	return Agent.Action.FORWARD	

# Turn agent to the left
def turnLeft( self ):
	Agent.Dir -= 1
	if Agent.Dir < 0:
		Agent.Dir = 3

	Agent.Moved = False
	return Agent.Action.TURN_LEFT

# Turn agent to the right
def turnRight( self ):
	Agent.Dir += 1
	if Agent.Dir > 3:
		Agent.Dir = 0

	Agent.Moved = False
	return Agent.Action.TURN_RIGHT

def markWall( self ):
	# Mark upper wall
	if Agent.Dir == 0:
		for x in range(0, 7):
			Agent.Map[x][Agent.y + 1] = 'Wall'
	# Mark right wall
	if Agent.Dir == 1:
		for y in range(0, 7):
			Agent.Map[Agent.x + 1][y] = 'Wall'	

Agent.getNext = MethodType(getNext, Agent)
Agent.markPit = MethodType(markPit, Agent)
Agent.markWump = MethodType(markWump, Agent)
Agent.moveFow = MethodType(moveFow, Agent)
Agent.turnLeft = MethodType(turnLeft, Agent)
Agent.turnRight = MethodType(turnRight, Agent)
Agent.markWall = MethodType(markWall, Agent)
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================