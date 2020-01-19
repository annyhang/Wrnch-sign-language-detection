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


#if finger is straight, true; else false
istraightIndex= True if IPIPy > IDIPy and IDIPy > IPIPy else False
istraightMiddle= True if MPIPy > MDIPy and MDIPy > MPIPy else False
istraightRing= True if RPIPy > RDIPy and RDIPy > RPIPy else False
istraightPointer= True if PPIPy > PDIPy and PDIPy > PPIPy else False
   

#for o, r
def isItSuperimposed():
  print("Hello from a function")