from math import pow


class ZNInteger:
    def __init__(self, integer, dividers):
        self.zn_value = {}
        for divider in dividers:
            self.zn_value[divider] = integer % divider

    def add(self, integer):
        for divider, value in self.zn_value.items():
            self.zn_value[divider] = (value + integer) % int(divider)

    def multiply(self, integer):
        for divider, value in self.zn_value.items():
            self.zn_value[divider] = (value * integer) % int(divider)

    def power(self, integer):
        for divider, value in self.zn_value.items():
            self.zn_value[divider] =  pow(value, integer) % int(divider)

    def get_value(self, divider):
        return self.zn_value[divider]
