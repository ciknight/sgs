# -*- coding: utf-8 -*-
import random
from typing import List

from card import Category, Package, Suit, Type


class Card():
    """ 卡牌

    Args:
        name: 卡牌名字
        type: 卡牌类型
        category: 卡牌种类
        suit: 卡牌花色
        number: 卡牌大小
        package: 卡牌包名
    """

    def __init__(
        self,
        *,
        name: str,
        type: Type,
        category: Category,
        suit: Suit,
        number: int,
        package: Package,
    ) -> None:
        self._name = name
        self._type = type
        self._category = category
        self._suit = suit
        self._number = number
        self._package = package

    @property
    def name(self):
        return self._name

    def serialize(self) -> dict:
        return dict(
            name=self._name,
            type=self._type,
            category=self._category,
            suit=self._suit,
            number=self._number,
            package=self._package,
        )


class CardPile():
    """ 牌堆

    Args:
        packages: 卡牌包
        cards: 卡牌列表
    """

    def __init__(self, packages: List[Package] = None, cards: List[Card] = None) -> None:
        self._packages = packages or []
        self._cards: List[Card] = cards or []

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        assert self._cards, 'cards is empty'
        random.shuffle(self._cards)

    def append(self, card: Card):
        assert isinstance(card, Card)
        self._cards.append(card)

    def initialize(self):
        from card.data import raw_cards
        for package in self._packages:
            for raw_card in raw_cards[package]:
                self.append(Card(**raw_card, package=package))

        self.shuffle()
