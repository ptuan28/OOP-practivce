class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = 0.0
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self._celsius = value
        else:
            raise ValueError

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9
        self.celsius = self._celsius