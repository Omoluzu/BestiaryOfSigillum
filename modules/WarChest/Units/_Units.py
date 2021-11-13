#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Юниты
"""
from abc import ABC


class Units(ABC):
    name = None  # Кодовое имя юнита
    translate = None  # Имя юнита на русском языке

    def __repr__(self):
        return f"<class Units({self.__class__.__name__}) translate={self.translate} >"
