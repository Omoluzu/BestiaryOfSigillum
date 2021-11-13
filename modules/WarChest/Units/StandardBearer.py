#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Знаменосец
"""

from ._Units import Units


class StandardBearer(Units):

    def name(self):
        return "StandardBearer"

    def translate(self):
        return "Знаменосец"
