#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Маршалы
"""

from ._Units import Units


class Marshal(Units):

    def name(self):
        return "Marshal"

    def translate(self):
        return "Маршалы"
