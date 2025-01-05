#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve
from controller_input import ControllerInput
from pid_controller import PIDController

controller = PIDController(
    kp_x=20.0, ki_x=0.0, kd_x=40.0,
    kp_y=1.0, ki_y=0.0, kd_y=10.0,
    kp_z=20.0, ki_z=0.0, kd_z=40.0,
    player_input_gain_x=2.0, player_input_gain_y=1.0, player_input_gain_z=2.0
)

async def on_plant_output_received(websocket):
    global controller
    print(f"Client connected: {websocket.remote_address}")
    async for message in websocket:
        controller_input = ControllerInput(message)
        controller_output = controller.step(controller_input)
        await websocket.send(controller_output.to_bytes())

async def main():
    print("Starting WebSocket server...")
    async with serve(on_plant_output_received, "localhost", 8765) as server:
        await server.serve_forever()

asyncio.run(main())