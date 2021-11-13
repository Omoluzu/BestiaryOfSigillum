#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лучники
"""

from ._Units import Units


class Archers(Units):

    def name(self):
        return "Archers"

    def translate(self):
        return "Лучники"
