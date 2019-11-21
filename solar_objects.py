# coding: utf-8
# license: GPLv3


class Star:
	def __init__(self):
		self.x = 0
		self.type = 'Star'
		self.y = 0
		self.Vx = 0
		self.Vy = 0
		self.Fx = 0
		self.Fy = 0
		self.R = 0
		self.color = None
		self.image = None
    
	"""Тип данных, описывающий звезду.
	Содержит массу, координаты, скорость звезды,
	а также визуальный радиус звезды в пикселах и её цвет.
	"""


class Planet:
    def __init__(self):
        self.x = 0
        self.type = 'Planet'
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 0
        self.color = None
        self.image = None

    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """