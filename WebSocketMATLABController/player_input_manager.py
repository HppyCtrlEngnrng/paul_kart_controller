import keyboard

class PlayerInputManager:
    @staticmethod
    def get_input():
        player_input_x = 0
        player_input_y = 0
        player_input_z = 0

        if keyboard.is_pressed('a'):
            player_input_z = -1
        if keyboard.is_pressed('d'):
            player_input_z = 1
        if keyboard.is_pressed('w'):
            player_input_x = -1
        if keyboard.is_pressed('s'):
            player_input_x = 1
        if keyboard.is_pressed('e'):
            player_input_y = 1
        if keyboard.is_pressed('q'):
            player_input_y = -1
        
        return player_input_x, player_input_y, player_input_z