#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def csipog(self):
        self.ev3.speaker.beep()

    def touchSensorFeladat(self):
        while(self.ts.pressed() == False):
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)
