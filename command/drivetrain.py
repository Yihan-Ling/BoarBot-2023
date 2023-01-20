from robotpy_toolkit_7407.command import SubsystemCommand

from subsystem import Drivetrain

from oi.keymap import Keymap

from robot_systems import Robot

import time

from wpilib import AnalogEncoder




class Zero(SubsystemCommand[Drivetrain]):
    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem
        self.left_forward_zeroed = False
        self.left_back_zeroed = False
        self.right_forward_zeroed = False
        self.right_back_zeroed = False

    def initialize(self):

        # self.initial_pos1 = Robot.drivetrain.left_forward_turn.get_sensor_position()
        # self.target_pos1 = self.initial_pos1 +
        self.pos_diff1 = self.convert(
            (Robot.drivetrain.left_forward_abs_encoder.getAbsolutePosition()-0.575) *360)

        self.initial_pos2 = Robot.drivetrain.left_back_turn.get_sensor_position()
        self.target_pos2 = self.initial_pos2 + self.convert(
            (Robot.drivetrain.left_back_abs_encoder.getAbsolutePosition()-0.988) * 360)

        self.initial_pos3 = Robot.drivetrain.right_forward_turn.get_sensor_position()
        self.target_pos3 = self.initial_pos3 + self.convert(
            (Robot.drivetrain.right_forward_abs_encoder.getAbsolutePosition() - 0.399) * 360)

        self.initial_pos4 = Robot.drivetrain.right_back_turn.get_sensor_position()
        self.target_pos4 = self.initial_pos4 + self.convert(
            (Robot.drivetrain.right_back_abs_encoder.getAbsolutePosition()-0.582) * 360)

        Robot.drivetrain.left_forward_turn.set_sensor_position(80)


    def execute(self):
        # if Robot.drivetrain.left_forward_turn.get_sensor_position() >= self.target_pos1:
        #     self.left_forward_zeroed = True
        #     Robot.drivetrain.left_forward_turn.set_raw_output(0)
        #
        # if Robot.drivetrain.left_back_turn.get_sensor_position() >= self.target_pos2:
        #     self.left_back_zeroed = True
        #     Robot.drivetrain.left_back_turn.set_raw_output(0)
        #
        # if Robot.drivetrain.right_forward_turn.get_sensor_position() >= self.target_pos3:
        #     self.right_forward_zeroed = True
        #     Robot.drivetrain.right_forward_turn.set_raw_output(0)
        #
        # if Robot.drivetrain.right_back_turn.get_sensor_position() >= self.target_pos4:
        #     self.right_back_zeroed = True
        #     Robot.drivetrain.left_back_turn.set_raw_output(0)

        # if abs(Robot.drivetrain.left_forward_abs_encoder.getAbsolutePosition()-0.575) <= 0.005:
        #     self.left_forward_zeroed = True
        #     Robot.drivetrain.left_forward_turn.set_raw_output(0)
        #
        # if abs(Robot.drivetrain.left_back_abs_encoder.getAbsolutePosition()-0.988) <= 0.005:
        #     self.left_back_zeroed = True
        #     Robot.drivetrain.left_back_turn.set_raw_output(0)
        #
        # if abs(Robot.drivetrain.right_forward_abs_encoder.getAbsolutePosition()-0.399) <= 0.005:
        #     self.right_forward_zeroed = True
        #     Robot.drivetrain.right_forward_turn.set_raw_output(0)
        #
        # if abs(Robot.drivetrain.right_back_abs_encoder.getAbsolutePosition()-0.582) <= 0.005:
        #     self.right_back_zeroed = True
        #     Robot.drivetrain.right_back_turn.set_raw_output(0)

        # if not self.left_forward_zeroed:
        #     Robot.drivetrain.left_forward_turn.set_raw_output(0.25)
        #
        # if not self.left_back_zeroed:
        #     Robot.drivetrain.left_back_turn.set_raw_output(0.25)
        #
        # if not self.right_forward_zeroed:
        #     Robot.drivetrain.right_forward_turn.set_raw_output(0.25)
        #
        # if not self.right_back_zeroed:
        #     Robot.drivetrain.right_back_turn.set_raw_output(0.25)

        Robot.drivetrain.left_forward_turn.set_target_position(0)
        Robot.drivetrain.left_forward_turn.set_raw_output(-0.25)
        print(Robot.drivetrain.left_forward_turn.get_sensor_position())



        # print(Robot.drivetrain.right_forward_abs_encoder.getAbsolutePosition())

    def end(self, interrupted=False):
        # print(AnalogEncoder(2).getAbsolutePosition())
        # Robot.drivetrain.left_forward_turn.set_raw_output(0)
        # Robot.drivetrain.left_back_turn.set_raw_output(0)
        # Robot.drivetrain.right_forward_turn.set_raw_output(0)
        # Robot.drivetrain.right_back_turn.set_raw_output(0)
        # print(Robot.drivetrain.left_forward_abs_encoder.getAbsolutePosition())
        # print(Robot.drivetrain.left_back_abs_encoder.getAbsolutePosition())
        # print(Robot.drivetrain.right_forward_abs_encoder.getAbsolutePosition())
        # print(Robot.drivetrain.right_back_abs_encoder.getAbsolutePosition())
        print(Robot.drivetrain.left_forward_turn.get_sensor_position())
        Robot.drivetrain.left_forward_turn.set_raw_output(0)

    def isFinished(self):
        # if self.left_forward_zeroed and self.left_back_zeroed and self.right_forward_zeroed and self.right_back_zeroed:
        #     return True
        return False

        # return Robot.drivetrain.left_forward_turn.get_sensor_position() <= 0

    def convert(self, degree):
        return 80.4848*degree/360


class Turn(SubsystemCommand[Drivetrain]):
    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self):
        self.initial_pos = Robot.drivetrain.right_forward_turn.get_sensor_position()
        self.target_pos = self.initial_pos + self.convert(90)
        print("target: "+str(self.target_pos))
        Robot.drivetrain.facing = 1

    def execute(self):
        Robot.drivetrain.right_forward_turn.set_raw_output(0.25)
        Robot.drivetrain.right_back_turn.set_raw_output(0.25)
        Robot.drivetrain.left_forward_turn.set_raw_output(0.25)
        Robot.drivetrain.left_back_turn.set_raw_output(0.25)

    def end(self, interrupted=False):
        Robot.drivetrain.right_forward_turn.set_raw_output(0)
        Robot.drivetrain.right_back_turn.set_raw_output(0)
        Robot.drivetrain.left_forward_turn.set_raw_output(0)
        Robot.drivetrain.left_back_turn.set_raw_output(0)

    def isFinished(self):
        print(Robot.drivetrain.right_forward_turn.get_sensor_position())
        return abs(Robot.drivetrain.right_forward_turn.get_sensor_position() - self.initial_pos) >= self.convert(90)

    def convert(self, degree):
        return 80.4848*degree/360




class TankDrive(SubsystemCommand[Drivetrain]):
    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self):
        ...

    def execute(self):

        L_Speed = Keymap.Drivetrain.Left_Wheels_Speed.value
        R_Speed = Keymap.Drivetrain.Right_Wheels_Speed.value

        if abs(L_Speed) < 0.2:
            L_Speed = 0
        if abs(R_Speed) < 0.2:
            R_Speed = 0

        if(Robot.drivetrain.facing==0):
            Robot.drivetrain.left_forward.set_raw_output(L_Speed)
            Robot.drivetrain.left_back.set_raw_output(L_Speed)
            Robot.drivetrain.right_forward.set_raw_output(R_Speed)
            Robot.drivetrain.right_back.set_raw_output(R_Speed)

        if(Robot.drivetrain.facing==1):
            Robot.drivetrain.left_forward.set_raw_output(L_Speed)
            Robot.drivetrain.left_back.set_raw_output(R_Speed)
            Robot.drivetrain.right_forward.set_raw_output(L_Speed)
            Robot.drivetrain.right_back.set_raw_output(R_Speed)

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False


class Forward(SubsystemCommand[Drivetrain]):
    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self):
        self.sTime = time.time()

    def execute(self):
        # print("run")
        Robot.drivetrain.left_forward.set_raw_output(0.5)
        Robot.drivetrain.left_back.set_raw_output(0.5)
        Robot.drivetrain.right_forward.set_raw_output(0.5)
        Robot.drivetrain.right_back.set_raw_output(0.5)

    def end(self, interrupted=False):
        Robot.drivetrain.left_forward.set_raw_output(0)
        Robot.drivetrain.left_back.set_raw_output(0)
        Robot.drivetrain.right_forward.set_raw_output(0)
        Robot.drivetrain.right_back.set_raw_output(0)

    def isFinished(self):
        timeElapsed = time.time()-self.sTime
        # print(timeElapsed)
        return timeElapsed > 1.5