import struct

class ControllerInput:
    def __init__(self, plant_output: bytes):
        self.controller_reset_flag = plant_output[0] == b'\x01'
        (
            self.pole_rotation_x,
            self.pole_rotation_y,
            self.pole_rotation_z,
            self.pole_angular_velocity_x,
            self.pole_angular_velocity_y,
            self.pole_angular_velocity_z,
            self.wheel_angular_velocity_x,
            self.wheel_angular_velocity_y,
            self.wheel_angular_velocity_z,
            self.flywheel_angular_velocity_y ) = struct.unpack('ffffffffff', plant_output[1:])