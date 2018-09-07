import random

inventory=[]
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
    if direc in rooms[currentLocation]:
      currentLocation= rooms[currentLocation][direc]
      print('%s is at: %s' % (self.name, currentLocation))
    else:
      print('u cant move there')
  
  def look(self):
    if len(rooms[currentLocation]['suelo']) > 0:
      print(rooms[currentLocation]['suelo'])
    else:
      print('no hay nada interesante..') 
  
  def take
  
  
  def n(self):
    self.move('norte')
  def s(self):
    self.move('sur')
  def e(self):
    self.move('este')
  def o(self):
    self.move('oeste')

comandos={'norte':Player.n,
          'sur':Player.s,
          'este':Player.e,
          'oeste':Player.o,
          'look':Player.look}

p1=Player()
p1.name=input('type ur name')
while (p1.moral > 0):
  line= input('>')
  arg=line.split()
  if len(arg) >0:
    for i in comandos.keys():
      if arg[0]==i[:len(arg[0])]:
        comandos[i](p1)
        break
