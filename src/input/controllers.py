class GenericController:
    def __init__(self):
        self.mapping = {
            "a": "left",
            "d": "right",
            "w": "forward",
            "s": "backward",
            "space": "jump",
        }

    def map(self, input_signal):
        return self.mapping.get(input_signal, input_signal)
