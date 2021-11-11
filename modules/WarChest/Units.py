#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Юниты
"""
from abc import ABC, abstractmethod


class Units(ABC):

    @property
    @abstractmethod
    def name(self):
        return None

    @property
    @abstractmethod
    def translate(self):
        return None


class Crossbowman(Units):

    def name(self):
        return "Crossbowman"

    def translate(self):
        return "Арбалетчики"


class RoyalGuard(Units):

    def name(self):
        return "RoyalGuard"

    def translate(self):
        return "Королевская гвардия"


class Mercenaries(Units):

    def name(self):
        return "Mercenaries"

    def translate(self):
        return "Наемники"


class Pikemen(Units):

    def name(self):
        return "Pikemen"

    def translate(self):
        return "Пикинеры"


class Marshal(Units):

    def name(self):
        return "Marshal"

    def translate(self):
        return "Маршалы"


class Cavalry(Units):

    def name(self):
        return "Cavalry"

    def translate(self):
        return "Кавалерия"


class Spearmen(Units):

    def name(self):
        return "Spearmen"

    def translate(self):
        return "Копейщики"


class StandardBearer(Units):

    def name(self):
        return "StandardBearer"

    def translate(self):
        return "Знаменосец"


class LightCavalry(Units):

    def name(self):
        return "LightCavalry"

    def translate(self):
        return "Легкая кавалерия"


class Berserkers(Units):

    def name(self):
        return "Berserkers"

    def translate(self):
        return "Берсерки"


class Archers(Units):

    def name(self):
        return "Archers"

    def translate(self):
        return "Лучники"


class Infantry(Units):

    def name(self):
        return "Infantry"

    def translate(self):
        return "Пехота"


class Knights(Units):

    def name(self):
        return "Knights"

    def translate(self):
        return "Рыцари"


class Scouts(Units):

    def name(self):
        return "Scouts"

    def translate(self):
        return "Разведчики"


class Swordsmen(Units):

    def name(self):
        return "Swordsmen"

    def translate(self):
        return "Мечники"


class Chaplain(Units):

    def name(self):
        return "Chaplain"

    def translate(self):
        return "Капеланы"



