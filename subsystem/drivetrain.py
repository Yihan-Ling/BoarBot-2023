from robotpy_toolkit_7407.motors.rev_motors import SparkMax
from commands2 import Subsystem
from wpilib import AnalogEncoder
from wpilib import cim

# class SparkMaxConfig

# class CIM():
#     def __init__(self, can_id: int, inverted: bool = True, brushless: bool = True, config: SparkMaxConfig = None):
#         pass


class Drivetrain(Subsystem):
    # Motors
    def __init__(self):
        super().__init__()
        self.left_cim1 = CIM(1)
        self.left_forward = SparkMax(1)
        self.left_back = SparkMax(7)
        self.right_forward = SparkMax(3)
        self.right_back = SparkMax(5)
        self.right_forward_turn = SparkMax(4)
        self.left_forward_turn = SparkMax(2)
        self.left_back_turn = SparkMax(8)
        self.right_back_turn = SparkMax(6)


        self.left_forward_abs_encoder = AnalogEncoder(0)
        self.right_forward_abs_encoder = AnalogEncoder(3)
        self.left_back_abs_encoder = AnalogEncoder(1)
        self.right_back_abs_encoder = AnalogEncoder(2)

        self.left_forward.init()
        self.left_back.init()
        self.right_forward.init()
        self.right_back.init()
        self.right_forward_turn.init()
        self.left_forward_turn.init()
        self.left_back_turn.init()
        self.right_back_turn.init()


    # self.left_forward.set_raw_output(0.5)
    # self.left_back.set_raw_output(0.5)
    # self.right_forward.set_raw_output(0.5)
    # self.right_back.set_raw_output(0.5)


