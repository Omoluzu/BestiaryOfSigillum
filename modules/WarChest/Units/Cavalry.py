#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Кавалерия
"""

from ._Units import Units


class Cavalry(Units):

    def name(self):
        return "Cavalry"

    def translate(self):
        return "Кавалерия"
