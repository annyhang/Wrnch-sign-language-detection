import math
import json
import sys

def json_r(resp_get_job):
   with open(resp_get_job) as f_in:
       return(json.load(f_in))

def init(resp_get_job):
    pose_estimation = json_r(resp_get_job)
   
    hand_pose = pose_estimation['frames'][0]['persons'][0]

   
    Wristx = hand_pose['hand_pose']['right']['joints'][0]
    Wristy = hand_pose['hand_pose']['right']['joints'][1]
    TMCPx = hand_pose['hand_pose']['right']['joints'][2]
    TMCPy =hand_pose['hand_pose']['right']['joints'][3]
    IMCPx =hand_pose['hand_pose']['right']['joints'][4]
    IMCPy =hand_pose['hand_pose']['right']['joints'][5]
    MMCPx = hand_pose['hand_pose']['right']['joints'][6]
    MMCPy = hand_pose['hand_pose']['right']['joints'][7]
    RMCPx = hand_pose['hand_pose']['right']['joints'][8]
    RMCPy = hand_pose['hand_pose']['right']['joints'][9]
    PMCPx = hand_pose['hand_pose']['right']['joints'][10]
    PMCPy = hand_pose['hand_pose']['right']['joints'][11]
    TPIPx=hand_pose['hand_pose']['right']['joints'][12]
    TPIPy=hand_pose['hand_pose']['right']['joints'][13]
    TDIPx= hand_pose['hand_pose']['right']['joints'][14]
    TDIPy= hand_pose['hand_pose']['right']['joints'][15]
    TTIPx=hand_pose['hand_pose']['right']['joints'][16]
    TTIPy=hand_pose['hand_pose']['right']['joints'][17]
    IPIPx=hand_pose['hand_pose']['right']['joints'][18]
    IPIPy=hand_pose['hand_pose']['right']['joints'][19]
    IDIPx=hand_pose['hand_pose']['right']['joints'][20]
    IDIPy=hand_pose['hand_pose']['right']['joints'][21]
    ITIPx= hand_pose['hand_pose']['right']['joints'][22]
    ITIPy=hand_pose['hand_pose']['right']['joints'][23]
    MPIPx= hand_pose['hand_pose']['right']['joints'][24]
    MPIPy= hand_pose['hand_pose']['right']['joints'][25]
    MDIPx= hand_pose['hand_pose']['right']['joints'][26]
    MDIPy= hand_pose['hand_pose']['right']['joints'][27]
    MTIPx=hand_pose['hand_pose']['right']['joints'][28]
    MTIPy= hand_pose['hand_pose']['right']['joints'][29]
    RPIPx= hand_pose['hand_pose']['right']['joints'][30]
    RPIPy=hand_pose['hand_pose']['right']['joints'][31]
    RDIPx=hand_pose['hand_pose']['right']['joints'][32]
    RDIPy= hand_pose['hand_pose']['right']['joints'][33]
    RTIPx= hand_pose['hand_pose']['right']['joints'][34]
    RTIPy= hand_pose['hand_pose']['right']['joints'][35]
    PPIPx=hand_pose['hand_pose']['right']['joints'][36]
    PPIPy= hand_pose['hand_pose']['right']['joints'][37]
    PDIPx= hand_pose['hand_pose']['right']['joints'][38]
    PDIPy= hand_pose['hand_pose']['right']['joints'][39]
    PTIPx= hand_pose['hand_pose']['right']['joints'][40]
    PTIPy=hand_pose['hand_pose']['right']['joints'][41]
    TDIPscore=hand_pose['hand_pose']['right']['scores'][7]
    TTIPscore=hand_pose['hand_pose']['right']['scores'][8]
    
    def withinoverlap(a, b):
        if (a< b and a+0.015 >=b ) or (a>b and b+0.015 >=a):
            #within
            return True
        else:
            return False

    isverticalIndex= True if IPIPy > IDIPy and IDIPy > ITIPy and IPIPy > ITIPy and not withinoverlap(ITIPy, IDIPy) else False
    isverticalMiddle= True if MPIPy > MDIPy and MDIPy > MTIPy and MPIPy > MTIPy and not withinoverlap(MTIPy, MDIPy) else False
    isverticalRing= True if RPIPy > RDIPy and RDIPy > RTIPy  and RPIPy > RTIPy and not withinoverlap(RTIPy, RDIPy)  else False
    isverticalPinky= True if PPIPy > PDIPy and PDIPy > PTIPy and PPIPy > PTIPy and not withinoverlap(PTIPy, PDIPy) else False

   
    #now for thumb:  vertical / curved / hidden
#need scores for TDIP and TTIP

# 0 for hidden, 1 for curved, 2 for vertical


    def isThumb():
        
        if TPIPy > TDIPy and TDIPy > TTIPy and TTIPy < IMCPy:
            # vertical
            return 2
        elif TDIPscore < 0.9 and TTIPscore < 0.9:
            #hidden
            return 0
        else:
            #curved, not hidden
            return 1
   
    thumb = isThumb()



    #for o, r
    #0.015 overlap
    # returns o or r or none
   

    def testSuperimposed():
        #for o, index and thumb should be touching, rest should be on same y level
        #also fingers shouldnt be straight
        if withinoverlap(ITIPy, TTIPy) and withinoverlap(ITIPx, TTIPx)\
        and withinoverlap(MTIPy, TTIPy)and withinoverlap(RTIPy, TTIPy)\
        and withinoverlap(PTIPy, TTIPy) and not isverticalIndex \
        and not isverticalMiddle and not isverticalRing \
        and not isverticalPinky:
            
            print("Sign is o")
            return 'o'
            quit()
        #for r, if index and middle DIPs are crossed, straight
        # rest are bent      
        elif withinoverlap (IDIPx, MDIPx) and withinoverlap (IDIPy, MDIPy)\
        and isverticalMiddle and isverticalIndex\
        and not isverticalRing and not isverticalPinky:
           
            print("Sign is r") 
            return 'r'
            quit()


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
        and thumb == 1:
            
            print("Sign is b")
            return 'b'
            quit()
        #3 f
        elif isverticalPinky and isverticalRing\
        and isverticalMiddle and not isverticalIndex\
        and withinoverlap (TTIPy, ITIPy) and withinoverlap (TTIPx, ITIPx):
          
            print("Sign is f")  
            return 'f'
            quit()
        #3 w
        elif isverticalIndex and isverticalMiddle and isverticalRing\
        and not isverticalPinky:
           
            print("Sign is w") 
            return 'w'
            quit()
        #2 k
        elif isverticalIndex and isverticalMiddle and not isverticalRing\
        and not isverticalPinky and thumb ==2:
            
            print("Sign is k")
            return 'k'
            quit()
        #2 u 
        # same x level for the vertical fingers
        # so im going to cheat the angle thing
        # via finding the gap between the fingers, if did not increase u
        #otherwise v 
        elif isverticalIndex and isverticalMiddle and not isverticalRing\
        and not isverticalPinky and withinoverlap(math.fabs(IPIPx-MPIPx), math.fabs(ITIPx-MTIPx)):
            print("Sign is u")
            return 'u'           
            quit()
        #2 v
        elif isverticalIndex and isverticalMiddle and not isverticalRing \
        and not isverticalPinky:      
            print("Sign is v")
            return 'v'
            quit()
        #1 index
        elif isverticalIndex and not isverticalMiddle and not isverticalRing\
        and not isverticalPinky:
            #l
            if (TTIPx > IMCPx and TTIPx > PMCPx) or (TTIPx < IMCPx and TTIPx < PMCPx):
                print("Sign is l")
                return 'l'                
                quit()
            # d, z
            else:
               
                print("Sign is d or z") 
                return 'd'
                quit()
        #1 pinky
        elif isverticalPinky and not isverticalMiddle and not isverticalRing\
        and not isverticalIndex:
            #y
            if (TTIPx > IMCPx and TTIPx > PMCPx) or (TTIPx < IMCPx and TTIPx < PMCPx):
                
                print("Sign is y")
                return 'y'
                quit()
            #i, j
            else:
                
                print("Sign is i or j")
                return 'i'
                quit()

    # horizontal straight g or h or p
    # downwards straight q
    def testOtherStraights():
        #g or h or p
        if ((ITIPx > IDIPx and ITIPx > IPIPx and IDIPx > IPIPx) or (ITIPx < IDIPx and ITIPx < IPIPx and IDIPx < IPIPx)) \
        and not withinoverlap(ITIPy, IDIPy) and not withinoverlap(MTIPy, MDIPy) \
        and not isverticalRing and not isverticalPinky and thumb !=2 and not withinoverlap(ITIPx, IDIPx): 
            if ((MTIPx > MDIPx and MTIPx > MPIPx and MDIPx > MPIPx ) or (MTIPx < MDIPx and MTIPx < MPIPx and MDIPx < MPIPx)\
            and not withinoverlap(MTIPx, MDIPx)):
                print (isverticalIndex)
                
                print("Sign is h")
                return 'h'
                quit()
            # p 
            # middle finger points down
            elif MPIPy < MDIPy and MDIPy < MTIPy:
                
                print("Sign is p") 
                return p
                quit()
            else:
               
                print("Sign is g") 
                return 'g'
                quit()
        #q
        elif IPIPy < IDIPy and IDIPy < ITIPy and TTIPy > TDIPy:
            
            print("Sign is q")
            return 'q'
            quit()


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
            
            print("Sign is t")
            return 't'
            quit()
        #c
        elif ITIPy < IMCPy and MTIPy < MMCPy and RTIPy < RMCPy and PTIPy < PMCPy \
        and TTIPy > IPIPy:
            
            print("Sign is c")
            return 'c'
            quit()
        #x
        elif ITIPy < MPIPy:
            
            print ("Sign is x")
            return 'x'
            quit()
        #n
        elif ITIPy < RDIPy and MTIPy < RDIPy:
            
            print ("Sign is n")
            return 'n'
            quit()
        #m
        elif ITIPy < PDIPy and MTIPy < PDIPy and RTIPy < PDIPy :
            
            print ("Sign is m")    
            return 'm'
            quit()
        #a 
        elif (thumb==2 )and TTIPy < IPIPy:
           
            print ("Sign is a") 
            return 'a'
            quit()
        #e
        elif ITIPy < TTIPy and MTIPy < TTIPy:
            
            print ("Sign is e")
            return 'e'
            quit()
        #s
        else:
            
            print ("Sign is s")
            return 's'
            quit()




    def main():  
        testSuperimposed()
        testvertical()
        testOtherStraights()
        testCurved()

    thumb = isThumb()
    main()

init(sys.argv[1])


    

    

