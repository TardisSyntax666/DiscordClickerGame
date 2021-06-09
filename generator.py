import pygame
import math


class Generator:

    def __init__(self, starting_cost, starting_product, growth_rate, starting_rev):
        self.starting_cost = starting_cost
        self.starting_product = starting_product
        self.growth_rate = growth_rate
        self.starting_rev = starting_rev
        self.owned = 0
        self.cost = int(self.starting_cost)
        self.production = int(self.starting_product)

    def upgrade(self):
        self.owned += 1
        self.cost = int(float(self.starting_cost) * math.pow(float(self.growth_rate), float(self.owned)))
        self.production = int(float(self.starting_product) * float(self.owned) * float(self.starting_rev))

