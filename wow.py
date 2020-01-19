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
# returns o or r or none
def isItSuperimposed():
  if 
