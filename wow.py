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


istraightIndex= True if IPIPy > IDIPy and IDIPy > ITIPy else False
istraightMiddle= True if MPIPy > MDIPy and MDIPy > MTIPy else False
istraightRing= True if RPIPy > RDIPy and RDIPy > RTIPy else False
istraightPointer= True if PPIPy > PDIPy and PDIPy > PTIPy else False

#now for thumb:  straigh / curved / hidden
#need scores for TDIP and TTIP
TDIPscore
TTIPscore
# 0 for hidden, 1 for curved, 2 for straight
thumb = -1

def isThumb():
    if TPIPy > TDIPy and TDIPy > TTIPy:
        # straight
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

def isItSuperimposed():
    #for o, index and thumb should be touching, rest should be on same y level
    #also fingers shouldnt be straight
    if withinoverlap(ITIPy, TTIPy) and withinoverlap(ITIPx, TTIPx)\
    and withinoverlap(MTIPy, TTIPy)and withinoverlap(RTIPy, TTIPy)\
    and withinoverlap(PTIPy, TTIPy) and not istraightIndex \
    and not istraightMiddle and not istraightRing \
    and not istraightPointer:
          return 'o'
    #for r, if index and middle DIPs are crossed, straight
    # rest are bent      
    elif withinoverlap (IDIPx, MDIPx) and withinoverlap (IDIPy, MDIPy)\
    and istraightMiddle and istraightIndex\
    and not istraightRing and not istraightPointer:
        return 'r'
    else:
        return None

#next, deal with the straight fingers
#function to count how many we have

# 4 is b
# 3 is f or w
# 2 is k or u or v
# 1 is z or y or l or i or j or d
# horizontal straight g or h or p
# downwards straight q
# all curled straight thumb a
# all curled curled / hidden thumb x or t or s or n or m or c or e

def main():
    isThumb()
    if isItSuperimposed()=='r':
        print("The sign is r!")
    elif isItSuperimposed()=='o':
        print("The sign is o!")
    else 

