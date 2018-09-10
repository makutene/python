import random

inventory={}
currentLocation='fosmet'

rooms={
        'fosmet':{
                  'norte':'nutcha',
                  'oeste':'pasillo hacia R15',
                  'suelo':['diphoterine','detector h2s','hombre al suelo']},
        'nutcha':{'sur':'fosmet',
                  'suelo':[]},
        'pasillo hacia R15':{
                  'este':'fosmet',
                  'oeste':'R15',
                  'suelo':['cigarro']},
        'R15':{
                'este':'pasillo hacia R15',
                'sur':'salida hacia una vida mejor!',
                'suelo':['pala']}}



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

  def move(self, direc):
    global currentLocation
    if random.randint(0,1):
      Paco.checkInv(self)
    if direc in rooms[currentLocation]:
      currentLocation= rooms[currentLocation][direc]
      print('%s is at: %s' % (self.name, currentLocation))
    else:
      print('No puedes ir en esa dirección')
  
  def look(self):
    if len(rooms[currentLocation]['suelo']) > 0:
      print(rooms[currentLocation]['suelo'])
    else:
      print('no hay nada interesante..') 
  
  def rest(self):
    if self.moral < self.moral_max:
      self.moral += 1
    else:
      print('Has descansado demasiado...')

  def status(self):
    print('La moral de %s: %d/%d' % (self.name, self.moral, self.moral_max))

  def take(self):
    obj=input('que objeto quieres? >')
    if obj in rooms[currentLocation]['suelo']:
      if obj in inventory.keys():
        inventory[obj]+=1
        rooms[currentLocation]['suelo'].remove(obj)
      else:
        inventory.setdefault(obj,1)  
    else:
      print('El objeto que quieres no está')
  
  def inv(self):
    print(inventory)

  def n(self):
    self.move('norte')
  def s(self):
    self.move('sur')
  def e(self):
    self.move('este')
  def o(self):
    self.move('oeste')

class Enemy(Char):
  def __init__(self):
    super().__init__()
  def low_moral(self):
    damage= random.randint(0,self.moral)
    self.moral -= damage
    if damage == 0:
      self.moral_max += 1
      print('no te dejas humillar')
    else:
      print('%s Tu moral es: %d/%d' % (self.name, self.moral, self.moral_max))

class Paco(Enemy):
  def __init__(self):
    super().__init__()
  def checkInv(self):
    if 'cigarro' in inventory.keys():
      print('Te cruzas con Paco. Hazme un porrito %s' % self.name)
      inventory['cigarro']-=1
      Enemy.low_moral(self)
    else:
      print('Te cruzas con Paco. Vaya veo que no tienes cigarritos..')


comandos={'norte':Player.n,
          'sur':Player.s,
          'este':Player.e,
          'oeste':Player.o,
          'look':Player.look,
          'take':Player.take,
          'inv':Player.inv,
          'status':Player.status,
          'rest':Player.rest}


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
  p1.name=input('Como te llamas? > ')
  while (p1.moral > 0):
    line= input('>')
    arg=line.split()
    if len(arg) >0:
      for i in comandos.keys():
        if arg[0]==i[:len(arg[0])]:
          comandos[i](p1)
          break

main()
