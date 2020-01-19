import math

Wristx
Wristy
TMCPx
TMCPy
IMCPx
IMCPy
MMCPx
MMCPy
RMCPx
RMCPy
PMCPx
PMCPy
TPIPx
TPIPy
TDIPx
TDIPy
TTIPx
TTIPy
IPIPx
IPIPy
IDIPx
IDIPy
ITIPx
ITIPy
MPIPx
MPIPy
MDIPx
MDIPy
MTIPx
MTIPy
RPIPx
RPIPy
RDIPx
RDIPy
RTIPx
RTIPy
PPIPx
PPIPy
PDIPx
PDIPy
PTIPx
PTIPy


isverticalIndex= True if IPIPy > IDIPy and IDIPy > ITIPy else False
isverticalMiddle= True if MPIPy > MDIPy and MDIPy > MTIPy else False
isverticalRing= True if RPIPy > RDIPy and RDIPy > RTIPy else False
isverticalPinky= True if PPIPy > PDIPy and PDIPy > PTIPy else False

#now for thumb:  vertical / curved / hidden
#need scores for TDIP and TTIP
TDIPscore
TTIPscore
# 0 for hidden, 1 for curved, 2 for vertical
thumb = -1

def isThumb():
    if TPIPy > TDIPy and TDIPy > TTIPy and withinoverlap(TPIPx, TDIPx) \
    and withinoverlap(TDIPx and TTIPx):
        # vertical
        thumb = 2
    elif TDIPscore < 0.9 and TTIPscore < 0.9:
        #hidden
        thumb = 0
    else:
        #curved, not hidden
        thumb = 1
   

#for o, r
#0.015 overlap
# returns o or r or none
def withinoverlap(a, b):
    if (a< b and a+0.15 >=b ) or (a>b and b+0.15 >=a):
        #within
        return True
    else:
        return False

def testSuperimposed():
    #for o, index and thumb should be touching, rest should be on same y level
    #also fingers shouldnt be straight
    if withinoverlap(ITIPy, TTIPy) and withinoverlap(ITIPx, TTIPx)\
    and withinoverlap(MTIPy, TTIPy)and withinoverlap(RTIPy, TTIPy)\
    and withinoverlap(PTIPy, TTIPy) and not isverticalIndex \
    and not isverticalMiddle and not isverticalRing \
    and not isverticalPinky:
          #return 'o'
          print("Sign is r")
    #for r, if index and middle DIPs are crossed, straight
    # rest are bent      
    elif withinoverlap (IDIPx, MDIPx) and withinoverlap (IDIPy, MDIPy)\
    and isverticalMiddle and isverticalIndex\
    and not isverticalRing and not isverticalPinky:
        #return 'r'
        print("Sign is o")


#next, deal with the straight fingers
#function to count how many we have

# 4 is b
# 3 is f or w
# 2 is k or u or v
# 1 is z or y or l or i or j or d
    #z and d index thumb in
    # y pinky thumb out
    #i  and j pinky thumb in
    # l index thumb out
# horizontal straight g or h or p
# downwards straight q
# all curled straight thumb a
# all curled curled / hidden thumb x or t or s or n or m or c or e

def testvertical():
    #4
    if isverticalMiddle and isverticalIndex\
    and isverticalPinky and isverticalRing\
    and thumb == 2:
        #return 'b'
        print("Sign is b")
    #3 f
    elif isverticalPinky and isverticalRing\
    and isverticalMiddle and not isverticalIndex\
    and withinoverlap (TTIPy, ITIPy) and withinoverlap (TTIPx, ITIPx):
        #return 'f'
        print("Sign is f")
    #3 w
    elif isverticalIndex and isverticalMiddle and isverticalRing\
    and not isverticalPinky:
        #return 'w'
        print("Sign is w")
    #2 k
    elif isverticalIndex and isverticalMiddle and not isverticalRing\
    and not isverticalPinky and thumb ==2:
        #return 'k'
        print("Sign is k")
    #2 u 
    # same x level for the vertical fingers
    # so im going to cheat the angle thing
    # via finding the gap between the fingers, if did not increase u
    #otherwise v 
    elif isverticalIndex and isverticalMiddle and not isverticalRing\
    and not isverticalPinky and withinoverlap(math.fabs(IPIPx-MPIPx), math.fabs(ITIPx-MTIPx)):
        #return 'u'
        print("Sign is u")
    #2 v
    elif isverticalIndex and isverticalMiddle and not isverticalRing \
    and not isverticalPinky:
        #return 'v'
        print("Sign is v")
    #1 index
    elif isverticalIndex and not isverticalMiddle and not isverticalRing\
    and not isverticalPinky:
        #l
        if (TTIPx > IMCPx and TTIPx > PMCPx) or (TTIPx < IMCPx and TTIPx < PMCPx):
            #return 'l'
            print("Sign is l")
        # d, z
        else:
            #return 'd'
            print("Sign is d or z")
    #1 pinky
    elif isverticalPinky and not isverticalMiddle and not isverticalRing\
    and not isverticalIndex:
        #y
        if (TTIPx > IMCPx and TTIPx > PMCPx) or (TTIPx < IMCPx and TTIPx < PMCPx):
            #return 'y'
            print("Sign is y")
        #i, j
        else:
            #return 'i'
            print("Sign is i or j")

# horizontal straight g or h or p
# downwards straight q
def testOtherStraights():
    #g or h or p
    if (ITIPX > IDIPX and ITIPX > IPIPx) or (ITIPX < IDIPX and ITIPX < IPIPx) \
    and not isverticalRing and not isverticalPinky: 
        if (MTIPX > MDIPX and MTIPX > MPIPx) or (MTIPX < MDIPX and MTIPX < MPIPx):
            #return 'h'
            print("Sign is h")
        # p 
        # middle finger points down
        elif MPIPy < MDIPy and MDIPy < MTIPy:
            #return p
            print("Sign is p") 
        else:
            #return 'g'
            print("Sign is g")
    #q
    elif IPIPy < IDIPy and IDIPy < ITIPy:
        #return q
        print("Sign is q")


# all curled straight thumb a
# t thumb between index and middle
# s thumb tip inside
# n index and middle one level, others level below
# m index and middle and ring one level, pinky below
# c tips over MCP
# e thumb tip overlap w middle / ring finger
# x index finger one level, others level below

def testCurved():
    #t
    if (TTIPx < IPIPx and TTIPx > MPIPx) or (TTIPx > IPIPx and TTIPx < MPIPx) \
    and TTIPy < PPIPy:
        # return t
        print("Sign is t")
    #c
    elif ITIPy < IMCPy and MTIPy < MMCPy and RTIPy < RMCPy and PTIPy < PMCPy \
    and TTIPy > IPIPy:
        #return c
        print("Sign is c")
    #x
    elif ITIPy < MPIPy:
        #return x
        print ("Sign is x")
    #n
    elif ITIPy < RDIPy and MTIPy < RDIPy:
        # return n
        print ("Sign is n")
    #m
    elif ITIPy < PDIPy and MTIPy < PDIPy and RTIPy < PDIPy :
        # return m
        print ("Sign is m")    
    #a 
    elif thumb == 2 and TTIPy < IPIPy:
        #return a
        print ("Sign is a")
    #e
    elif ITIPy < TTIPy and MTIPy < TTIPy:
        #return e
        print ("Sign is e")
    #s
    else:
        #return s
        print ("Sign is s")




def main():
    isThumb()
    testSuperimposed()
    testvertical()
    testOtherStraights()
    testCurved()



    

