# -*- coding: utf-8 -*-

from enum import Enum, auto

__all__ = ['Card', 'CardPile', 'Package', 'Suit', 'Category', 'Type']


class Package(Enum):
    """ 卡包，标准包、EX包"""
    standard = auto()
    ex = auto()


class Suit(Enum):
    """ 卡牌花色 """
    spade = auto()  # 黑桃
    heart = auto()  # 红桃
    club = auto()  # 梅花
    diamond = auto()  # 方片


class Category(Enum):
    """ 卡牌类型 """
    basic = auto()  # 标准
    tip = auto()  # 普通锦囊
    delayed_tip = auto()  # 延时锦囊
    equipment = auto()  # 装备


class Equiment(Enum):
    hanbingjian = auto()  # 寒冰剑


class Type(Enum):
    """ 卡牌种类 """
    # 普通牌
    kill = auto()  # 杀
    dodge = auto()  # 闪
    heal = auto()  # 桃

    # 锦囊牌
    duel = auto()  # 决斗
    dismantle = auto()  # 过河拆桥
    steal = auto()  # 顺手牵羊
    more = auto()  # 无中生有
    borrow = auto()  # 借刀杀人
    imok = auto()  # 无懈可击，EX

    allkill = auto()  # 南蛮入侵
    alldodge = auto()  # 万箭齐发
    allheal = auto()  # 桃园结义
    allmore = auto()  # 五谷丰登

    # 延时锦囊
    rest = auto()  # 乐不思蜀
    thunder = auto()  # 闪电，EX

    # 装备
    weapon = auto()  # 武器
    shield = auto()  # 护盾
    attack_horse = auto()  # 攻击马
    defense_horse = auto()  # 防御马
    artifact = auto()  # 宝物


from card.card import Card, CardPile  # noqa, isort:skip
