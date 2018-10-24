from math import sqrt, pow, atan2, pi, fmod, sin, tan, cos


def roundAngle(angle):
    """

    Args:
        angle:

    Returns:

    """

    theta = fmod(angle,  2 * pi)

    if theta > pi:
        theta = theta - (2 * pi)
    elif theta < -pi:
        theta = theta + (2 * pi)

    return theta


def saturate(value):
    """

    Args:
        value:

    Returns:

    """

    if value > 1:
        value = 1
    elif value < -1:
        value = -1

    return value


class Dice:
    """
    Attributes:
        warrior:
        maxThetaError (float):
    """

    def __init__(self):
        self.warrior = None
        self.maxThetaError = roundAngle(20.0*pi/180)

    def run(self, warrior):
        """

        Args:
            warrior:

        Returns:

        """

        self.warrior = warrior
        self.warrior.vMax = round(self.warrior.vMax * 100) / 100

        if warrior.cmdType == "VECTOR":
            return self.vectorControl()
        elif warrior.cmdType == "POSITION":
            return self.positionControl()
        elif warrior.cmdType == "ORIENTATION":
            return self.orientationControl()
        elif warrior.cmdType == "SPEED":
            return self.speedControl()
        else:
            raise ValueError("Invalid cmdType")

    def vectorControl(self):
        """
        Returns:
        """
        if self.warrior.vMax == 0:
            return [0.0, 0.0]

        # theta = float(atan2(sin(self.warrior.orientation - (-self.warrior.transAngle)),
        #                     cos(self.warrior.orientation - (-self.warrior.transAngle))) * 180 / pi)
        # theta = round(theta * 100) / 100

        # target = [50 * cos(theta * pi/180), 50 * sin(theta * pi/180)]
        # targetTheta = atan2(target[1] - self.warrior.position[1], target[0] - self.warrior.position[0])
        targetTheta = self.warrior.transAngle
        theta = self.warrior.orientation
        moveBackwards = bool(abs(targetTheta - self.warrior.orientation) > pi/2)
        if moveBackwards:
            theta = roundAngle(self.warrior.orientation + pi)

        thetaError = roundAngle(targetTheta - theta)

        if moveBackwards:
            self.warrior.vLeft = -1 - sin(thetaError) + (-1 * tan(thetaError/2))
            self.warrior.vLeft = saturate(self.warrior.vLeft)

            self.warrior.vRight = -1 + sin(thetaError) + (-1 * tan(-1 * thetaError / 2))
            self.warrior.vRight = saturate(self.warrior.vRight)
        else:
            self.warrior.vLeft = 1 - sin(thetaError) + tan(-1 * thetaError / 2)
            self.warrior.vLeft = saturate(self.warrior.vLeft)

            self.warrior.vRight = 1 + sin(thetaError) + tan(thetaError / 2)
            self.warrior.vRight = saturate(self.warrior.vRight)

        return [self.warrior.vLeft, self.warrior.vRight]

    def positionControl(self):
        """
        Returns:
        """
        if self.warrior.target[0] == -1 and self.warrior.target[1] == -1:
            return [0.0, 0.0]

        targetTheta = atan2((self.warrior.target[1] - self.warrior.position[1])*1.3 / 480,
                            -(self.warrior.target[0] - self.warrior.position[0])*1.5 / 640)
        currentTheta = atan2(sin(self.warrior.orientation), cos(self.warrior.orientation))

        if atan2(sin(targetTheta - currentTheta + pi/2), cos(targetTheta - currentTheta + pi/2)) < 0:
            backward = True
            m = 1
        else:
            backward = False
            m = -1

        if backward:
            currentTheta = currentTheta + pi
            currentTheta = atan2(sin(currentTheta), cos(currentTheta))

        thetaError = atan2(sin(targetTheta - currentTheta), cos(targetTheta - currentTheta))

        left = m + sin(thetaError)
        right = m - sin(thetaError)

        left = saturate(left)
        right = saturate(right)

        left = self.warrior.vMax * left
        right = self.warrior.vMax * right

        return [left, right]

    def orientationControl(self):
        """
        Returns:
        """
        targetTheta = self.warrior.targetOrientation

        theta = self.warrior.orientation

        # É necessário girar se estiver com a 'traseira' de frente pro alvo? (Se sim, não usar o if abaixo)
        if roundAngle(targetTheta - self.warrior.orientation + pi/2) < 0:
            theta = roundAngle(self.warrior.orientation + pi)

        thetaError = roundAngle(targetTheta - theta)

        if abs(thetaError) < 2*pi/180:
            return [0.0, 0.0]

        self.warrior.vLeft = saturate(0.8 * thetaError)
        self.warrior.vRight = saturate(-0.8 * thetaError)

        return [float(self.warrior.vLeft * self.warrior.vMax),
                float(self.warrior.vRight * self.warrior.vMax)]

    def speedControl(self):
        """
        Returns:
        """

        return [float(round(self.warrior.vLeft * 100) / 100),
                float(round(self.warrior.vRight * 100) / 100)]
