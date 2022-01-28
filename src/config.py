class Config():
    def __init__(self):
        self.movement_halted=False 
        self.audio_return_dict = {}
        self.avg_initial_coeff = []
        self.current_distance = 1000
        self.person_detected=False

config_obj = Config()