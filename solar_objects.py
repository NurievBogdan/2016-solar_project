# coding: utf-8
# license: GPLv3


class Star:
    def __init__(self, type, m, x, y, Vx, Vy, Fx, Fy, R, color, image):
    self.x = x
    self.type = type
    self.y = y
    self.Vx = x
    self.Vy = y
    self.Fx = x
    self.Fy = y
    self.R = R
    self.color = color
    self.image = image
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """


class Planet:
    def __init__(self, type, m, x, y, Vx, Vy, Fx, Fy, R, color, image):
    self.x = x
    self.type = type
    self.y = y
    self.Vx = x
    self.Vy = y
    self.Fx = x
    self.Fy = y
    self.R = R
    self.color = color
    self.image = image
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """