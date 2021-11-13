#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Арбалетчик
"""

from ._Units import Units


class Crossbowman(Units):

    def name(self):
        return "Crossbowman"

    def translate(self):
        return "Арбалетчики"
