class Luffy:
    def __init__(self):
        self.card_name='Luffy'
        self.lvl=1
        self.exp=0
        self.hp=31
        self.atk = 29
        self.defence= 32
        self.spd = 24
        self.spdef=18
        self.spatk=18
        self.love=1
        self.critical = 1
        self.image="https://cdn.discordapp.com/attachments/811481352050311178/828937111058776064/a20e90107b7f8ad4001fd7808e53f51d.png"
        self.evasion = 1
        self.total = 150
        self.series=1
        self.atype="Active"

        self.ability = 'Reflection'
        self.ability_desc = 'It absorbs and help in reflecting the enemy atk. increasing card defence by 25% and decreases speed by 10%'
    def ability_worker(self,card):
        if card.procc == 2:
            card.spd = card.spd - 90/100
            card.defence = card.defence * 125/100
            card.procc=0
            return "increasing card defence by 25% and decreases speed by 10%"

class Naruto:
    def __init__(self):
        self.card_name = 'Naruto'
        self.lvl=1
        self.exp=0
        self.hp=29
        self.atk = 19
        self.defence= 21
        self.spd = 31
        self.spdef=22
        self.spatk=28
        self.love=1
        self.critical = 1
        self.image="https://cdn.discordapp.com/attachments/811481352050311178/828937620029177946/1775702.png"
        self.evasion = 1
        self.total = 150
        self.series=2
        self.atype="Active"
        self.ability = 'Talk no jutsu'
        self.ability_desc = 'It makes the enemy unstable due to emotion outburst. increasing spdef and def each by 10% and also increasing atk by 15%'
    def ability_worker(self,card):
        if card.procc==2:
            card.atk = card.atk_base * 115/100
            card.spdef = card.spdef_base * 110/100
            card.defence = card.defence_base * 110/100
            card.procc=0
            return "increasing spdef and def each by 10% and also increasing atk by 15%'"



class Emiya:
    def __init__(self):
        self.card_name='Emiya'
        self.lvl=1
        self.exp=0
        self.hp=24
        self.atk = 31
        self.defence= 23
        self.spd = 25
        self.spdef=20
        self.spatk=27
        self.love=1
        self.critical = 1
        self.image="https://cdn.discordapp.com/attachments/811481352050311178/828937765168218122/01120EMIYA204.png"
        self.evasion = 1
        self.total = 150
        self.series=3
        self.atype="Active"
        self.ability = "Mind's Eye"
        self.ability_desc = 'Enhances senses and increase chance of evasion by 28%'

    def ability_worker(self,card):
        if card.procc==3:
            if card.evasion<70:
                card.evasion = card.evasion + 28 
            else:
                pass
            card.procc=0
            return "increasing chance of evasion by 28%"

class Hercules:
    def __init__(self):
        self.card_name='Hercules'
        self.lvl=1
        self.exp=0
        self.hp=35
        self.atk = 20
        self.defence= 13
        self.spd = 25
        self.spdef=30
        self.spatk=33
        self.love=1
        self.critical = 1
        self.evasion = 1
        self.total = 150
        self.series=3
        self.atype="Passive"
        self.image="https://cdn.discordapp.com/attachments/811481352050311178/828937860370792479/04720Heracles204.png"
        self.ability = "Battle Continuation"
        self.ability_desc = 'When defeated in battle, return with 10% hp and increase attack by 90%'
    def ability_worker(self,card):
        if card.hp<0 or card.hp==0:
           card.hp = card.hp_base * 10/100
           card.atk=card.atk*1.9 
           return "return with 10% hp and increase attack by 90%"


class Altria_Pendragon:
    def __init__(self):
        self.card_name='Altria Pendragon'
        self.lvl=1
        self.exp=0
        self.hp=28
        self.atk = 32
        self.defence= 33
        self.spd = 23
        self.spdef=20
        self.spatk=15
        self.love=1
        self.critical = 1
        self.evasion = 1
        self.total = 150
        self.series=3
        self.atype="Active"
        self.image="https://cdn.discordapp.com/attachments/811481352050311178/828938029866811442/Artoria4.png"
        self.ability = "intuition"
        self.ability_desc = 'Increases **critical chance** by 25% and evasion by 10%'
    def ability_worker(self,card):
        if card.procc==2:
            if card.critical<75:  
                card.critical = card.critical+25
            if card.evasion<70:
                card.evasion = card.evasion+10
            card.procc=0
            return "Increasing **critical chance** by 25% and evasion by 10%"

