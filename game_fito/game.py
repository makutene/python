import random

inventory=[]
currentLocation='fosmet'

rooms={
        'fosmet':{
                  'norte':'nutcha',
                  'oeste':'pasillo hacia R15',
                  'suelo':['diphoterine','detector h2s','hombre al            suelo']},
        'pasillo hacia R15':{
                  'este':'fosmet',
                  'oeste':'R15',
                  'suelo':['cigarro']},
        'R15':{
                'este':'pasillo hacia R15',
                'sur':'salida hacia una vida mejor!',
                'suelo':['pala']}
        
        }        
        

class Char:
  def __init__(self):
    self.name=''
    self.moral=1
    self.moral_max=1

class Player(Char):
  def __init__(self):
    Char.__init__(self)
    self.moral=10
    self.moral_max=10
  def status(self):
    print('%s moral: %d/%d' % (self.name,self.moral, self.moral_max))
  def quit(self):
    print('%s has died' % self.name)
  def printLoc(loc):
    print(loc)
  def move(direc):
    global currentLocation
    if direc in rooms[currentLocation]:
      currentLocation=rooms[currentLocation][direc]        
      


comandos={'status':Player.status,
          'quit':Player.quit,
          'loc':Player.printLoc,
          'n':Player.move('norte'),
          's':Player.move('sur'),
          'e':Player.move('este'),
          'o':Player.move('oeste')}


p= Player()
p.name=input('type your name: >')

while (p.moral > 0):
  line= input('>')
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in comandos.keys():
      if args[0] == c[:len(args[0])]:
        comandos[c](p)
        commandFound = True
        break
