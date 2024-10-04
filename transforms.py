class Transform:
    def __init__(self, level, multi, health):
        self.level = level
        self.multi = multi
        self.health = health

transforms = [
    Transform(1, 1.0, 0),
    Transform(50, 1.05, 2000),
    Transform(100, 1.1, 6000),
    Transform(150, 1.15, 16000),
    Transform(200, 1.21, 36000),
    Transform(400, 1.27, 66000),
    Transform(600, 1.34, 106000),
    Transform(800, 1.4, 166000),
    Transform(900, 1.47, 206000),
    Transform(1000, 1.55, 266000),
    Transform(1200, 1.62, 346000),
    Transform(1400, 1.71, 446000),
    Transform(1600, 1.79, 566000)
]
