# -*- coding: utf-8 -*-
from enum import Enum, auto


class Identity(Enum):
    """ 身份 """

    king = auto()  # 主攻
    loyal = auto()  # 忠臣
    rebel = auto()  # 反贼
    cheat = auto()  # 内奸
