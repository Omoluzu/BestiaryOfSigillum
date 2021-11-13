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

    def __repr__(self):
        return f"<class Units({self.__class__.__name__}) translate={self.translate} >"
