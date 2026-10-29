class InputMapper:
    def __init__(self):
        self.mouse = {"left_click": "mouse_button_left", "right_click": "mouse_button_right"}
        self.keyboard = {"w": "move_forward", "a": "move_left", "s": "move_back", "d": "move_right"}

    def map_mouse(self, key):
        return self.mouse.get(key, key)

    def map_keyboard(self, key):
        return self.keyboard.get(key, key)
