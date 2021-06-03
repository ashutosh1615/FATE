import math
import random
class sas():
  def __init__(self):
    self.spatk=0
    self.spdef=0
    self.atk=0
    self.defence=0
    self.critical = 1

cardatk=sas()
carddef=sas()
cardatk.spatk=int(60*(1/5)*5)
carddef.spdef=int(10*(1/5)*5)
carddef.defence=int(50*(1/5)*5)
cardatk.atk=int(30*(1/5)*5)
crit = 1
r = random.randint(1,10)
print(r)
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

if r == 10:
        dmgatk= round((((cardatk.atk/carddef.defence)*(cardatk.spatk/carddef.spdef)*10)/3)*150/100,1) 
        dmgspatk=round((((((cardatk.spatk**1/cardatk.spatk*math.log(cardatk.spatk)**sigmoid(cardatk.spatk))*cardatk.critical)*cardatk.spatk/3)/carddef.spdef)**(cardatk.spatk**1/carddef.spdef))**(((cardatk.spatk+carddef.spdef))**1/carddef.spdef) + cardatk.spatk, 1)   
        print(dmgatk)
        print(dmgspatk)

else:
        dmgatk= round((((cardatk.atk/carddef.defence)*(cardatk.spatk/carddef.spdef)*10)/3),1) 
        dmgspatk=round(((((cardatk.spatk**1/cardatk.spatk*math.log(cardatk.spatk)*cardatk.spatk/3))/carddef.spdef)**(cardatk.spatk**1/carddef.spdef))**(((cardatk.spatk+carddef.spdef))**1/carddef.spdef)*(3+cardatk.critical), 1)
        print(dmgatk)
        print(dmgspatk)

dmg=dmgatk+dmgspatk
print(round(dmg))        