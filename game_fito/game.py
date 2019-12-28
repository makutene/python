import random
import time
inventory = {}
currentLocation = 'fosmet'

rooms = {
    'fosmet': {
        'norte': 'nutcha',
        'oeste': 'Pasillo hacia R15',
        'este': 'Escaleras de la muerte',
        'suelo': ['llave 24/26', 'coca-cola de Paco', 'tanga de Action-man']
    },
    'vestuario': {
        'norte': 'R15',
        'suelo': {
            'cigarro': 10
        }
    },
    'nutcha': {
        'sur': 'fosmet',
        'suelo': {
            'detector h2s': 1,
            'hombre al suelo': 1,
            'diphoterine': 1
        }
    },
    'Pasillo hacia R15': {
        'este': 'fosmet',
        'oeste': 'R15',
        'suelo': []
    },
    'R15': {
        'este': 'Pasillo hacia R15',
        'oeste': 'vestuario',
        'suelo': ['cuaderno de notas']
    },
    'Escaleras de la muerte':{
        'oeste':'fosmet'
    }
}

frases = [
    'Miguel te sonrie.. :) mañana te toca doblar',
    'Te cruzas con Miguel....Hay que limpiar bombonas',
    'Otra vez Miguel... hay campaña de azinfos y has sido seleccionado... :)','Os estais poniendo muy gordos en disolución, mañana de noche a para el LUWA'
]

moreda=['Moreda te felicita por llevar todos los EPIS','Moreda te da la brasa por no llevar los EPIS']

paco=['Te cruzas con Paco..Veo que no tienes cigarritos','El canso de Paco.. hazme un porrito']

def texT(txt):
  for i in range(len(txt)):
    print(txt[i], sep=' ', end='',flush=True)
    time.sleep(0.1)
  print('\n')

class Char:
    def __init__(self):
        self.name = ''
        self.moral = 10
        self.moral_max = 10


class Player(Char):
    def __init__(self):
        super().__init__()
        self.moral = 10
        self.moral_max = 10

    def help(self):
        print(comandos.keys())

    def move(self, direc):
        global currentLocation
        a = random.randint(0, 4)
        if a == 0:
            Paco.checkInv(self)
        if a == 1:
            Miguel.tocarHuev(self)
        if a == 2:
            Moreda.insPec(self)
        if direc in rooms[currentLocation]:
            currentLocation = rooms[currentLocation][direc]
            print('%s está en: %s' % (self.name, currentLocation))
        else:
            print('No puedes ir en esa dirección')

    def look(self):
        if len(rooms[currentLocation]['suelo']) > 0:
            print(rooms[currentLocation]['suelo'])
        else:
            print('No hay nada interesante..')

    def rest(self):
        if currentLocation == 'vestuario':
            if self.moral < self.moral_max:
                self.moral += 1
                print('moral de %s: %d/%d' % (self.name, self.moral,
                                              self.moral_max))
            else:
                print('Has descansado mucho...')
        else:
            print('No puedes descansar aqui')

    def status(self):
        print('moral de %s: %d/%d' % (self.name, self.moral, self.moral_max))

    def take(self):
        obj = input('Que objeto quieres? >')
        if obj in rooms[currentLocation]['suelo']:
            if obj in inventory.keys():
                inventory[obj] += 1
                rooms[currentLocation]['suelo'][obj] -= 1
            else:
                inventory.setdefault(obj, 1)
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
        damage = random.randint(0, self.moral)
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
            texT(paco[1])
            inventory['cigarro'] -= 1
            Enemy.low_moral(self)
        else:
            texT(paco[0])

class Miguel(Enemy):
    def __init__(self):
        super().__init__()

    def tocarHuev(self):
        a = random.choice(frases)
        for i in range(len(a)):
            print(a[i], sep=' ', end='', flush=True)
            time.sleep(0.1)
        print('\n')    
        Enemy.low_moral(self)


class Moreda(Enemy):
    def __init__(self):
        super().__init__()

    def insPec(self):
        if ('diphoterine' and 'detector h2s'
                and 'hombre al suelo') in inventory.keys():
                texT(moreda[0])
                self.moral+=1
                print('%s moral: %d/%d' % (self.name, self.moral, self.moral_max))   
        else:
            texT(moreda[1])  
            Enemy.low_moral(self)


comandos = {
    'norte': Player.n,
    'sur': Player.s,
    'este': Player.e,
    'oeste': Player.o,
    'mirar': Player.look,
    'coger': Player.take,
    'inventario': Player.inv,
    'status': Player.status,
    'descansar': Player.rest,
    'ayuda': Player.help
}


def main():
    print('''
        
    Esto es ESCAPE FROM FITO
    
    consigue llegar a final de turno con tabaco y el móvil!!!
    
    Escribe ayuda para ver los comandos


  ''')

    p1 = Player()
    p1.name = input('Como te llamas? > ')
    while (p1.moral > 0):
        line = input('>')
        arg = line.split()
        if len(arg) > 0:
            for i in comandos.keys():
                if arg[0] == i[:len(arg[0])]:
                    comandos[i](p1)
                    break

    print('---------------------')
    print('Has perdido... Estás condenado a estar en Fito')
    print('---------------------')
    response = input('Jugar de nuevo? (s) / (n) >')
    if response == 's':
        main()
    else:
        pass


main()
