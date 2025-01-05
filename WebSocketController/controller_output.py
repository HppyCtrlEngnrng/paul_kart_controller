import struct

class ControllerOutput:
    def __init__(self, wheel_torque_x: float, flywheel_torque_y: float, wheel_torque_z: float):
        self.wheel_torque_x = wheel_torque_x
        self.flywheel_torque_y = flywheel_torque_y
        self.wheel_torque_z = wheel_torque_z

    def to_bytes(self) -> bytes:
        return struct.pack('fff',
            self.wheel_torque_x,
            self.flywheel_torque_y,
            self.wheel_torque_z)