import random

inventory={}
currentLocation='fosmet'

rooms={
        'fosmet':{
                  'north':'nutcha',
                  'west':'R15 corridor',
                  'ground':['diphoterine','detector h2s','man down']},
        'nutcha':{'south':'fosmet',
                  'ground':[]},
        'R15 corridor':{
                  'east':'fosmet',
                  'west':'R15',
                  'ground':['cigar']},
        'R15':{
                'east':'R15 corridor',
                'south':'escape to better life',
                'ground':['shovel']}}



class Char:
  def __init__(self):
    self.name= ''
    self.moral= 10
    self.moral_max= 10

class Player(Char):
  def __init__(self):
    super().__init__()
    self.moral=10
    self.moral_max=10

  def help(self):
    print(commands.keys())

  def move(self, direc):
    global currentLocation
    if random.randint(0,1):
      Paco.checkInv(self)
    if direc in rooms[currentLocation]:
      currentLocation= rooms[currentLocation][direc]
      print('%s is at: %s' % (self.name, currentLocation))
    else:
      print('You cant go this way')
  
  def look(self):
    if len(rooms[currentLocation]['ground']) > 0:
      print(rooms[currentLocation]['ground'])
    else:
      print('Theres nothing..') 
  
  def rest(self):
    if self.moral < self.moral_max:
      self.moral += 1
    else:
      print('You rested too much...')

  def status(self):
    print('%s moral: %d/%d' % (self.name, self.moral, self.moral_max))

  def take(self):
    obj=input('Which object you want? >')
    if obj in rooms[currentLocation]['ground']:
      if obj in inventory.keys():
        inventory[obj]+=1
        rooms[currentLocation]['ground'].remove(obj)
      else:
        inventory.setdefault(obj,1)  
    else:
      print('The object you want is not avaiable')
  
  def inv(self):
    print(inventory)

  def n(self):
    self.move('north')
  def s(self):
    self.move('south')
  def e(self):
    self.move('east')
  def o(self):
    self.move('west')

class Enemy(Char):
  def __init__(self):
    super().__init__()
  def low_moral(self):
    damage= random.randint(0,self.moral)
    self.moral -= damage
    if damage == 0:
      self.moral_max += 1
      print('you dont let be humiliated')
    else:
      print('%s moral: %d/%d' % (self.name, self.moral, self.moral_max))

class Paco(Enemy):
  def __init__(self):
    super().__init__()
  def checkInv(self):
    if 'cigar' in inventory.keys():
      print('You face Paco... Give me some cigar %s' % self.name)
      inventory['cigar']-=1
      Enemy.low_moral(self)
    else:
      print('You face Paco.. Ohh you dont have cigars')

comandos={'north':Player.n,
          'south':Player.s,
          'east':Player.e,
          'west':Player.o,
          'look':Player.look,
          'take':Player.take,
          'inv':Player.inv,
          'status':Player.status,
          'rest':Player.rest,
          'help':Player.help}

def main():
  print('''

                                    __                        __ _ _        
                                   / _|                      / _(_) |       
   ___  ___  ___ __ _ _ __   ___  | |_ _ __ ___  _ __ ___   | |_ _| |_ ___  
  / _ \/ __|/ __/ _` | '_ \ / _ \ |  _| '__/ _ \| '_ ` _ \  |  _| | __/ _ \ 
 |  __/\__ \ (_| (_| | |_) |  __/ | | | | | (_) | | | | | | | | | | || (_) |
  \___||___/\___\__,_| .__/ \___| |_| |_|  \___/|_| |_| |_| |_| |_|\__\___/ 
                     | |                                                    
                     |_|                                                    

  ''')

  p1=Player()
  p1.name=input('Whats your name? > ')
  while (p1.moral > 0):
    line= input('>')
    arg=line.split()
    if len(arg) >0:
      for i in comandos.keys():
        if arg[0]==i[:len(arg[0])]:
          comandos[i](p1)
          break

main()
