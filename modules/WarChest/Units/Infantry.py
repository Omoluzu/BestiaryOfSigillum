#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пехота
"""

from ._Units import Units



class Infantry(Units):

    def name(self):
        return "Infantry"

    def translate(self):
        return "Пехота"
