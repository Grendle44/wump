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

    # def turnLeft( thing ):
    #   Dir += 1
    #   if Dir > 4:
    #       Dir = 0
    #   return thing.Action.TURN_LEFT
    # Dir = 1

    # def turnLeft( self ):
    #   Agent.Dir += 1


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

        # The agent's next tile
        Agent.next = Agent.getNext()

        # Wumpus alive or not
        Agent.WumpAlive = True

        # Agent has moved or not
        Agent.moved = False

        pass
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================

        # Update next tile
        Agent.next = Agent.getNext()

        if breeze and Agent.moved:
            Agent.Map[Agent.x][Agent.y] = 'B'
            
            # Agent.next = 'pP'
            if Agent.Dir == 0:
                # Agent ^
                Agent.Map[Agent.x + 1][Agent.y] = 'pP'
                Agent.Map[Agent.x - 1][Agent.y] = 'pP'
                Agent.Map[Agent.x][Agent.y + 1] = 'pP'
            if Agent.Dir == 1:
                # Agent ->
                
                Agent.Map[Agent.x + 1][Agent.y] = 'pP'
                Agent.Map[Agent.x][Agent.y - 1] = 'pP'
                Agent.Map[Agent.x][Agent.y + 1] = 'pP'
            if Agent.Dir == 2:
                # Agent v
                Agent.Map[Agent.x + 1][Agent.y] = 'pP'
                Agent.Map[Agent.x - 1][Agent.y] = 'pP'
                Agent.Map[Agent.x][Agent.y +1] = 'pP'
            if Agent.Dir == 3:
                # Agent <-
                Agent.Map[Agent.x][Agent.y + 1] = 'pP'
                Agent.Map[Agent.x - 1][Agent.y] = 'pP'
                Agent.Map[Agent.x][Agent.y - 1] = 'pP'

        if scream:
            Agent.WumpAlive = False


        if Agent.WumpAlive:
            if stench:
                Agent.Map[Agent.x][Agent.y] = 'S'
                Agent.moved = False
                return Agent.Action.SHOOT
    
        
        if glitter:
            Agent.moved = False
            return Agent.Action.GRAB

        if bump:
            return Agent.turnLeft()

        # If move forward

        if Agent.getNext() == 'pP' or Agent.getNext() == 'B':
            return Agent.turnLeft()

        # # Facing right
        # if Agent.Dir == 1:
        #   if Agent.Map[Agent.x + 1][Agent.y] == 'pP' or Agent.Map[Agent.x + 1][Agent.y] == 'B':
        #       return Agent.turnLeft()
        #   if Agent.x >= 3:
        #       return Agent.turnLeft()
        #   Agent.x += 1
        # # Facing down
        # elif Agent.Dir == 2:
        #   if Agent.Map[Agent.x][Agent.y - 1] == 'pP':
        #       return Agent.turnLeft()
        #   if Agent.y <=0:
        #       return Agent.turnLeft()
        #   Agent.y -= 1
        # # Facing left
        # elif Agent.Dir == 3:
        #   if Agent.Map[Agent.x - 1][Agent.y] == 'pP':
        #       return Agent.turnLeft()
        #   Agent.x -= 1
        # # Facing up
        # if Agent.Dir == 0:
        #   if Agent.Map[Agent.x][Agent.y + 1] == 'pP':
        #       return Agent.turnLeft()
        #   Agent.y += 1

        # Agent.moved = True
        # return Agent.Action.FORWARD
        return Agent.moveFow()
        # return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

    # def turnLeft( self ):
    #   Agent.Dir += 1
        # if Agent.Dir > 4:
        #   Agent.Dir = 0
        #   # print('What')
        #   return Agent.Action.TURN_LEFT

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

    Agent.moved = True
    return Agent.Action.FORWARD 

# Turn agent to the left
def turnLeft( self ):
    Agent.Dir -= 1
    if Agent.Dir < 0:
        Agent.Dir = 3

    Agent.moved = False
    return Agent.Action.TURN_LEFT

# Turn agent to the right
def turnRight( self ):
    Agent.Dir += 1
    if Agent.Dir < 3:
        Agent.Dir = 0

    Agent.moved = False
    return Agent.Action.TURN_RIGHT


Agent.getNext = MethodType(getNext, Agent)
Agent.moveFow = MethodType(moveFow, Agent)
Agent.turnLeft = MethodType(turnLeft, Agent)
Agent.turnRight = MethodType(turnRight, Agent)
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================






#include <iostream>
#include <stdio.h>
#include <math.h>
#include <iomanip>
using namespace std;

typedef double (*pMathFunc)(double x); // pointer to a math function
double myf(double x){
    // return sin(x);
    return pow(x, 3) - 10;
}
double mydf(double x){
    // return cos(x);
    return 3*(pow(x, 2));
}
double x2f(double x){
    return pow(x, 2);
}
double x2df(double x){
    return 2*x;
}
double x2ddf(double x){
    return 2;
}
double x3f(double x){
    return pow(x, 3);
}
double x3df(double x){
    return 3*(pow(x, 2));
}
double x3ddf(double x){
    return 6*x;
}
double sinf(double x){
    return sin(x);
}
double sindf(double x){
    return cos(x);
}
double sinddf(double x){
    return -sin(x);
}
double cosf(double x){
    return cos(x);
}
double cosdf(double x){
    return -sin(x);
}
double cos1f(double x){
    return cos(x)+1;
}
double cos1df(double x){
    return -sin(x);
}
double tanf(double x){
    return tan(x);
}
double tandf(double x){
    return pow(1/cos(x), 2);
}

double MyZero(double x0, pMathFunc f, pMathFunc fp){
    double thing, delt, m;
    thing = x0 - f(x0)/fp(x0);
    for (int i=0; i<10; i++){
        delt = thing;
        thing = thing - f(thing)/fp(thing);
        if (delt - thing == 0){
            
            // cout << "delt " << setprecision(52) << delt << endl;
            // cout << "x "<< setprecision(52) << thing << endl;
            cout << "Normal iteration " << i << endl;
            return thing;
        }
    }
    return thing;
}


double MyZero2(double x0, pMathFunc f, pMathFunc fp, pMathFunc fpp){
    double thing, delt, m;
    m = pow(fp(x0),2)/(pow(fp(x0),2)-f(x0)*fpp(x0));
    thing = x0 - f(x0)/fp(x0);
    for (int i=0; i<10; i++){
        delt = thing;
        thing = thing - m*f(thing)/fp(thing);
        m = pow(fp(thing),2)/(pow(fp(thing),2)-f(thing)*fpp(thing));
        if (delt - thing == 0){
            cout << "M iterations " << i << endl;
            return thing;
        }
    }
    return thing;
}

int main(){
//  double zero = MyZero(-10, myf, mydf);
//  printf("The zero of x occurs at x=%g\n", zero);
    double zeroSinm = MyZero2(1, sinf, sindf, sinddf);
    printf("Sin w M The zero of x occurs at x=%g\n", zeroSinm);
    double zeroSin = MyZero(1, sinf, sindf);
    printf("Sin sin The zero of x occurs at x=%g\n", zeroSin);
    double zeroCos = MyZero(1, cosf, cosdf);
    printf("Cos The zero of x occurs at x=%g\n", zeroCos);
    double zeroCos1 = MyZero(1, cos1f, cos1df);
    printf("Cos+1 The zero of x occurs at x=%g\n", zeroCos1);
    double zeroTan = MyZero(1, tanf, tandf);
    printf("Tan The zero of x occurs at x=%g\n", zeroTan);
    double zerox2m = MyZero2(1, x2f, x2df, x2ddf);
    printf("X^2 w M The zero of x occurs at x=%g\n", zerox2m);
    double zerox2 = MyZero(1, x2f, x2df);
    printf("X^2 The zero of x occurs at x=%g\n", zerox2);
    double zerox3m = MyZero2(1, x3f, x3df, x3ddf);
    printf("X^3 w M The zero of x occurs at x=%g\n", zerox3m);
    double zerox3 = MyZero(1, x3f, x3df);
    printf("X^3 The zero of x occurs at x=%g\n", zerox3);
}








#------------------------------------------------------------------



#include <iostream>
#include <stdio.h>
#include <math.h>
#include <iomanip>
using namespace std;

typedef double (*pMathFunc)(double x); // pointer to a math function
double myf(double x){
    // return sin(x);
    return pow(x, 3) - 10;
}
double mydf(double x){
    // return cos(x);
    return 3*(pow(x, 2));
}
double x2f(double x){
    return pow(x, 2);
}
double x2df(double x){
    return 2*x;
}
double x2ddf(double x){
    return 2;
}
double x3f(double x){
    return pow(x, 3);
}
double x3df(double x){
    return 3*(pow(x, 2));
}
double x3ddf(double x){
    return 6*x;
}
double sinf(double x){
    return sin(x);
}
double sindf(double x){
    return cos(x);
}
double sinddf(double x){
    return -sin(x);
}
double cosf(double x){
    return cos(x);
}
double cosdf(double x){
    return -sin(x);
}
double cosddf(double x){
    return -cos(x);
}
double cos1f(double x){
    return cos(x)+1;
}
double cos1df(double x){
    return -sin(x);
}
double tanf(double x){
    return tan(x);
}
double tandf(double x){
    return pow(1/cos(x), 2);
}

double MyZero(double x0, pMathFunc f, pMathFunc fp){
    double thing, delt, m;
    thing = x0 - f(x0)/fp(x0);
    for (int i=0; i<10000; i++){
        delt = thing;
        thing = thing - f(thing)/fp(thing);
        if (delt - thing == 0){
            
            // cout << "delt " << setprecision(52) << delt << endl;
            // cout << "x "<< setprecision(52) << thing << endl;
            cout << "Normal iteration " << i << endl;
            return thing;
        }
    }
    return thing;
}


double MyZero2(double x0, pMathFunc f, pMathFunc fp, pMathFunc fpp){
    // double thing, delt, m, thing0, thing2;
    double xn, xn1, xn2, delt, m;
    
    xn1 = x0;
    xn = x0 - f(x0)/fp(x0);

    // thing0 = x0;
    // thing = x0 - f(x0)/fp(x0);
    for (int i=1; i<10000; i++){
        delt = xn;

        // xn2 = xn1;
        // xn1 = xn;
        // xn = xn -f(xn)/fp(xn);
        if (i>2){
            xn2 = xn1;
            xn1 = xn;
            // m = (thing2 -thing)/(thing - thing0);
            m = (xn-xn1)/(xn1-xn2);
            xn = xn - m*f(xn)/fp(xn);
            cout << "M = " << m << endl;
        }else{
            xn2 = xn1;
            xn1 = xn;
            xn = xn - f(xn)/fp(xn);
        }

        if (delt - xn == 0){
            cout << "M iterations " << i << endl;
            cout << "Zero " << xn << endl;
            return xn;
        }
    }
    return xn;
}

int main(){
//  double zero = MyZero(-10, myf, mydf);
//  printf("The zero of x occurs at x=%g\n", zero);
    // double zeroSinm = MyZero2(1, sinf, sindf, sinddf);
    // printf("Sin w M The zero of x occurs at x=%g\n", zeroSinm);
    // double zeroSin = MyZero(1, sinf, sindf);
    // printf("Sin sin The zero of x occurs at x=%g\n", zeroSin);
    // double zeroCos = MyZero(1, cosf, cosdf);
    // printf("Cos The zero of x occurs at x=%g\n", zeroCos);
    // double zeroCos1 = MyZero(1, cos1f, cos1df);
    // printf("Cos+1 The zero of x occurs at x=%g\n", zeroCos1);
    // double zeroTan = MyZero(1, tanf, tandf);
    // printf("Tan The zero of x occurs at x=%g\n", zeroTan);
    // double zerox2m = MyZero2(1, x2f, x2df, x2ddf);
    // printf("X^2 w M The zero of x occurs at x=%g\n", zerox2m);
    // double zerox2 = MyZero(1, x2f, x2df);
    // printf("X^2 The zero of x occurs at x=%g\n", zerox2);
    // double zerox3m = MyZero2(1, x3f, x3df, x3ddf);
    // printf("X^3 w M The zero of x occurs at x=%g\n", zerox3m);
    // double zerox3 = MyZero(1, x3f, x3df);
    // printf("X^3 The zero of x occurs at x=%g\n", zerox3);

    double zeroCos1 = MyZero(1, cos1f, cosdf);

    double zeroCos1m = MyZero2(1, cos1f, cosdf, cosddf);
    double zeroX2 = MyZero(1, x2f, x2df);
    double zeroX2m = MyZero2(1, x2f, x2df, x2ddf);
    double zeroX3 = MyZero(1, x3f, x3df);
    double zeroX3m = MyZero2(1, x3f, x3df, x3ddf);


}
