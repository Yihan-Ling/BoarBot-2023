import commands2
import wpilib

# import autonomous
import command
import config
import constants
import robot_systems
import sensors
import subsystem
import utils
from oi.OI import OI

from robot_systems import Robot
from oi.keymap import Keymap

class _Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):

        commands2.CommandScheduler.getInstance().schedule(
            commands2.SequentialCommandGroup(
                command.Zero(robot_systems.Robot.drivetrain)
                # command.Forward(robot_systems.Robot.drivetrain),
                # command.TankDrive(robot_systems.Robot.drivetrain)
            )
        )
        # print("teleopInit")

        pass

    def teleopPeriodic(self):

        # L_Speed = Keymap.Drivetrain.Left_Wheels_Speed.value
        # R_Speed = Keymap.Drivetrain.Right_Wheels_Speed.value
        #
        # if abs(L_Speed) < 0.2:
        #     L_Speed=0
        # if abs(R_Speed) < 0.2:
        #     R_Speed=0
        #
        # Robot.drivetrain.left_forward.set_raw_output(L_Speed)
        # Robot.drivetrain.left_back.set_raw_output(L_Speed)
        # Robot.drivetrain.right_forward.set_raw_output(R_Speed)
        # Robot.drivetrain.right_back.set_raw_output(R_Speed)
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        Robot.drivetrain.left_forward.set_raw_output(0.5)
        Robot.drivetrain.left_back.set_raw_output(0.5)
        Robot.drivetrain.right_forward.set_raw_output(0.5)
        Robot.drivetrain.right_back.set_raw_output(0.5)
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(_Robot)
