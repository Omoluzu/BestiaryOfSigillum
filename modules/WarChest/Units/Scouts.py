#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Разведчики
"""

from ._Units import Units


class Scouts(Units):

    def name(self):
        return "Scouts"

    def translate(self):
        return "Разведчики"
