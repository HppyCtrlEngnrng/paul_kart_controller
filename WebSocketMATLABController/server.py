#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve
import matlab.engine
from controller_input import ControllerInput
from controller_output import ControllerOutput
from player_input_manager import PlayerInputManager

print("Starting MATLAB engine...")
eng = matlab.engine.start_matlab()

controller = eng.PIDController(
    20.0, 0.0, 40.0,
    1.0, 0.0, 10.0,
    20.0, 0.0, 40.0,
    2.0, 1.0, 2.0
)

async def on_plant_output_received(websocket):
    global controller
    print(f"Client connected: {websocket.remote_address}")
    async for message in websocket:
        controller_input = ControllerInput(message)
        player_input_x, player_input_y, player_input_z = PlayerInputManager.get_input()
        u = eng.Step(
            controller,
            controller_input.controller_reset_flag,
            controller_input.pole_rotation_x,
            controller_input.pole_angular_velocity_y,
            controller_input.pole_rotation_z,
            player_input_x,
            player_input_y,
            player_input_z,
            nargout=3
            )
        controller_output = ControllerOutput(u[0], u[1], u[2])
        await websocket.send(controller_output.to_bytes())

async def main():
    print("Listening to client connections...")
    async with serve(on_plant_output_received, "localhost", 7654) as server:
        await server.serve_forever()

print("Starting WebSocket server...")
asyncio.run(main())