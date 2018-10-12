from math import atan2, pi
from .navigation import UnivectorField


class Eunomia:
    # TODO(Luana) Definir um nome final para Actions e documentá-lo

    def __init__(self):
        self.uvf = UnivectorField()

    def setup(self, width=100):
        radius = 0.2*width/1.70

        # Espiral radius, m2g kr, ao k0, distance dmin, gaussian delta
        # self.uvf.updateConstants(radius, 0.7, 0.1, 0.05, 0.15)
        self.uvf.updateConstants(4.0, 4.9, 0.12, 5.0, 4.5)

    def run(self, warrior):
        if warrior.action[0] == "stop":
            warrior.cmdType = "SPEED"
            return self.stop(warrior)

        elif warrior.action[0] == "spin":
            warrior.cmdType = "SPEED"
            return self.spin(warrior)

        elif warrior.action[0] == "lookAt":
            warrior.cmdType = "ORIENTATION"
            warrior.targetOrientation = self.lookAt(warrior.action[1], warrior.target,  warrior.position, warrior.targetOrientation)
            return warrior

        elif warrior.action[0] == "goTo":
            warrior.cmdType = "VECTOR"
            return self.goTo(warrior)

    '''
    - {
        "command": stop,
        "data": {}
    }
    '''
    def stop(self, warrior):
        if warrior.before == 0:
            warrior.vMax = 0
            warrior.vLeft = 0
            warrior.vRight = 0

        else:
            # TODO(Luana) Fazer controle de desesceleração
            warrior.vMax = 0
            warrior.vLeft = 0
            warrior.vRight = 0

        return warrior

    '''
    - {
        "command": "spin",
        "data": { "velocity": X m/s, "direction": "clockwise" | "counter"
        }
    }
    '''
    def spin(self, warrior):
        if warrior.action[1] == "clockwise":
            warrior.vLeft = warrior.vMax
            warrior.vRight = -warrior.vMax
        else:
            warrior.vLeft = -warrior.vMax
            warrior.vRight = warrior.vMax

        return warrior

    '''
    - {
        "command": "lookAt",
        "data": {
            "pose": {
                "position": (x, y),  # opcional - é passado se o target for um ponto
                "orientation": θ radianos
            },
            "target": θ radianos | (x, y)
        }
    }
    '''
    def lookAt(self, where, target, position, orientation=None):
        if where is "orientation":
            return orientation

        elif where is "target":
            x = target[0] - position[0]
            y = target[1] - position[1]
            return atan2(y, -x)

        else:
            raise ValueError("Invalid data.")

    '''
    - {
        "command": "goTo",
        "data": {
            "obstacles": [(x, y)] # opcional - se passado, desviar de tais obstaclos
            "pose": {"position": (x, y), "orientation": θ radianos},
            "target": {"position": (x, y), "orientation": θ radianos | (x, y)},  # opcional - pode ser uma orientação final ou uma posição de lookAt
            "velocity": X m/s,  # opcional - se passado, sem before, é a velocidade constante / com before é velocidade padrão
            "before": X s  # se passado sem o velocity, usa a velocidade máxima do robô como teto
        }
    }
    '''
    def goTo(self, warrior):
        # Se o targetOrientation passado for um ponto, calcular o targetOrientation usando o lookAt
        if type(warrior.targetOrientation) is tuple:
            target = warrior.targetOrientation
            del warrior.targetOrientation
            warrior.targetOrientation = self.lookAt("target", target, warrior.position)

        # Verificar se existe obstáculos para se desviar
        if warrior.obstacles is not None:
            self.uvf.updateObstacles(warrior.obstacles, [[0, 0], [0, 0]])

        #  Verificar se existe um 'before' na chamada desse método
        time = None
        # if warrior.before is not None:
        #   time = warrior.before

        if time is None:
            # TODO(Luana) Sem aceleração ou eu quem controlo como será feito a aceleração?

            warrior.vRight = warrior.vMax
            warrior.vLeft = warrior.vMax
            print("\nwarrior ", list(warrior.position))
            print("Target ", list(warrior.target))

            uvf = self.uvf.getVec(list(warrior.position), [warrior.vLeft, warrior.vRight], list(warrior.target), warrior.targetOrientation)
            # uvf =
            print("UVF " + str(uvf))
        else:
            # TODO(Luana) Fazer verificação se é possível realizar o trajeto com o tempo requisitado
            pass

        return warrior