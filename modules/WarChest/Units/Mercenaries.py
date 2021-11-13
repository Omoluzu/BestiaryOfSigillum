#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Наемники
"""

from ._Units import Units


class Mercenaries(Units):

    def name(self):
        return "Mercenaries"

    def translate(self):
        return "Наемники"
