import random

inventory=[]
currentLocation='fosmet'

rooms={
        'fosmet':{
                  'norte':'nutcha',
                  'oeste':'pasillo hacia R15',
                  'suelo':['diphoterine','detector h2s','hombre al suelo']},
        'pasillo hacia R15':{
                  'este':'fosmet',
                  'oeste':'R15',
                  'suelo':['cigarro']},
        'R15':{
                'este':'pasillo hacia R15',
                'sur':'salida hacia una vida mejor!',
                'suelo':['pala']}}



class Char:
  def __init__(self, name, moral, moral_max):
    self.name= name
    self.moral= 10
    self.moral_max= 10

class Player(Char):
  def __init__(self,name, moral, moral_max, state):
    super().__init__(name, moral, moral_max)
    self.state= state
  
  def status(self):
    print('%s moral is: %d/%d' % (self.name, self.moral, self.moral_max))
  
  def move(self, direc):
    global currentLocation
    if direc in rooms[currentLocation]:
      currentLocation= rooms[currentLocation][direc]
      print('%s is at: %s' % (self.name, currentLocation))
    else:
      print('u cant move there')




