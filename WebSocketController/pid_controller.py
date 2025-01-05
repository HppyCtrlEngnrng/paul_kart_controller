from controller_input import ControllerInput
from controller_output import ControllerOutput
from controller_base import ControllerBase
from player_input_manager import PlayerInputManager

class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def step(self, error):
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

    def reset(self):
        self.prev_error = 0
        self.integral = 0

class PIDController(ControllerBase):
    def __init__(self, 
        kp_x, ki_x, kd_x,
        kp_y, ki_y, kd_y,
        kp_z, ki_z, kd_z,
        player_input_gain_x, player_input_gain_y, player_input_gain_z
    ):
        self.pid_x = PID(kp_x, ki_y, kd_x)
        self.pid_y = PID(kp_y, ki_y, kd_y)
        self.pid_z = PID(kp_z, ki_z, kd_z)

        self.player_input_gain_x = player_input_gain_x
        self.player_input_gain_y = player_input_gain_y
        self.player_input_gain_z = player_input_gain_z

    def step(self, controller_input: ControllerInput) -> ControllerOutput:
        if controller_input.controller_reset_flag:
            self.reset()

        player_input_x, player_input_y, player_input_z = PlayerInputManager.get_input()
            
        torque_x = self.pid_x.step(controller_input.pole_rotation_x) + self.player_input_gain_x * player_input_x
        torque_y = self.pid_y.step(self.player_input_gain_y * player_input_y - controller_input.pole_angular_velocity_y)
        torque_z = self.pid_z.step(controller_input.pole_rotation_z) + self.player_input_gain_z * player_input_z

        return ControllerOutput(torque_x, torque_y, torque_z)

    def reset(self):
        self.pid_x.reset()
        self.pid_y.reset()
        self.pid_z.reset()