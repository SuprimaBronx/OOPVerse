class Cars:
    def __init__(self):
        self.type = ''
        self.engine_power = 0
        self.global_weight = 0
        self.ratio = 0

    def ratio_calc(self):
        self.ratio = self.global_weight / self.engine_power



