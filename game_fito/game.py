import random

inventory={}
currentLocation='fosmet'

rooms={
        'fosmet':{
                  'norte':'nutcha',
                  'oeste':'Pasillo hacia R15',
                  'suelo':['diphoterine','detector h2s','hombre al suelo']},
        'nutcha':{'sur':'fosmet',
                  'suelo':[]},
        'Pasillo hacia R15':{
                  'este':'fosmet',
                  'oeste':'R15',
                  'suelo':['cigarro']},
        'R15':{
                'este':'Pasillo hacia R15',
                'south':'Eres libre!',
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

  def help(self):
    print(comandos.keys())

  def move(self, direc):
    global currentLocation
    if random.randint(0,1):
      Paco.checkInv(self)
    if direc in rooms[currentLocation]:
      currentLocation= rooms[currentLocation][direc]
      print('%s está en: %s' % (self.name, currentLocation))
    else:
      print('No puedes ir en esa dirección')
  
  def look(self):
    if len(rooms[currentLocation]['suelo']) > 0:
      print(rooms[currentLocation]['suelo'])
    else:
      print('No hay nada interesante..') 
  
  def rest(self):
    if self.moral < self.moral_max:
      self.moral += 1
      print('moral de %s: %d/%d' % (self.name, self.moral, self.moral_max))
    else:
      print('Has descansado mucho...')

  def status(self):
    print('moral de %s: %d/%d' % (self.name, self.moral, self.moral_max))

  def take(self):
    obj=input('Que objeto quieres? >')
    if obj in rooms[currentLocation]['suelo']:
      if obj in inventory.keys():
        inventory[obj]+=1
        rooms[currentLocation]['suelo'].remove(obj)
      else:
        inventory.setdefault(obj,1)  
    else:
      print('Ese objeto no está')
  
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
      print('No te dejas humillar')
    else:
      print('%s moral: %d/%d' % (self.name, self.moral, self.moral_max))

class Paco(Enemy):
  def __init__(self):
    super().__init__()
  def checkInv(self):
    if 'cigarro' in inventory.keys():
      print('Te encuentras con Paco... Hazme un porrito %s' % self.name)
      inventory['cigarro']-=1
      Enemy.low_moral(self)
    else:
      print('Te cruzas con Paco.. Veo que no tienes cigarritos')

comandos={'norte':Player.n,
          'sur':Player.s,
          'este':Player.e,
          'oeste':Player.o,
          'mirar':Player.look,
          'coger':Player.take,
          'inventario':Player.inv,
          'status':Player.status,
          'descansar':Player.rest,
          'ayuda':Player.help}

def main():
  print('''
        
    Esto es ESCAPE FROM FITO

    Escribe ayuda para ver los comandos


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
  print('---------------------')
  print('Has perdido... Estás condenado a estar en Fito')
  print('---------------------')
  response=input('Jugar de nuevo? (s) / (n) >')
  if response == 's':
    main()
  else:
    pass
main()
