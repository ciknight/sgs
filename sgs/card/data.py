# -*- coding: utf-8 -*-
"""
---标准包（108张）---
--手牌--
# 杀（30张）
黑桃：7、8（2张）、9（2张）、10（2张）
红桃：10（2张）、J
梅花：2、3、4、5、6、7、8（2张）、9（2张）、10（2张）、J（2张）
方片：6、7、8、9、10、K

# 闪 （15张）
红桃：2（2张）、K
方片：2（2张）、3、4、5、6、7、8、9、10、J（2张）

# 桃（8张）
红桃：3、4、6、7、8、9、Q
方片：Q

# 决斗（3张）
黑桃：A
梅花：A
方片：A

# 过河拆桥（6张）
黑桃：3、4、Q
红桃：Q
梅花：3、4

# 顺手牵羊（5张）
黑桃：3、4、J
方片：3、4

# 无中生有（4张）
红桃：7、8、9、J

# 借刀杀人（2张）
梅花：Q、K

# 无懈可击（3张）
黑桃：J
梅花：Q、K

# 无懈可击，EX
方片：Q

# 南蛮入侵（3张）
黑桃：7、K
梅花：K

# 万箭齐发
红桃：A

# 桃园结义
红桃：A

# 五谷丰登（2张）
红桃：3、4

# 乐不思蜀（3张）
黑桃：6
红桃：6
梅花：6

# 闪电
黑桃：A

# 闪电，EX
红桃：Q

--武器--
# 寒冰剑，EX
黑桃：2

# 仁王盾，EX
梅花：2

# 诸葛连弩（2张）
梅花：1
方片：1

# 八卦阵（2张）
黑桃：2
梅花：2

# 雌雄双股剑
黑桃：2

# 青龙偃月刀
黑桃：5

# 绝影（+1）
黑桃：5

# 的卢（+1）
梅花：5

# 青釭剑
黑桃：6

# 丈八蛇矛
黑桃：Q

# 大宛（-1）
黑桃：K

# 麒麟弓
红桃：5

# 赤兔（-1）
红桃：5

# 贯石斧
方片：5

# 方天画戟
方片：Q

# 爪黄飞电（+1）
红桃：K

# 紫骍（-1）
方片：K

---军争包---
# TODO


"""
from card import Category, Package, Suit, Type

standard_package = [
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 7,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 8,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 8,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 9,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 9,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.spade,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 11,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 2,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 3,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 4,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 5,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 6,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 7,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 8,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 8,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 9,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 9,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 11,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.club,
        'number': 11,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 6,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 7,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 8,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 9,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 10,
    },
    {
        'name': '杀',
        'type': Type.kill,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 13,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 2,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 2,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 13,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 2,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 2,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 3,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 4,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 5,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 6,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 7,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 8,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 9,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 10,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 11,
    },
    {
        'name': '闪',
        'type': Type.dodge,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 11,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 3,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 4,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 6,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 7,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 8,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 9,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.heart,
        'number': 12,
    },
    {
        'name': '桃',
        'type': Type.heal,
        'category': Category.basic,
        'suit': Suit.diamond,
        'number': 12,
    },
    {
        'name': '决斗',
        'type': Type.duel,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 1,
    },
    {
        'name': '决斗',
        'type': Type.duel,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 1,
    },
    {
        'name': '决斗',
        'type': Type.duel,
        'category': Category.tip,
        'suit': Suit.diamond,
        'number': 1,
    },
    {
        'name': '过河拆桥',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 3,
    },
    {
        'name': '过河拆桥',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 4,
    },
    {
        'name': '过河拆桥',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 12,
    },
    {
        'name': '过河拆桥',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 12,
    },
    {
        'name': '过河拆桥',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 3,
    },
    {
        'name': '过河拆桥',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 4,
    },
    {
        'name': '顺手牵羊',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 3,
    },
    {
        'name': '顺手牵羊',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 4,
    },
    {
        'name': '顺手牵羊',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 11,
    },
    {
        'name': '顺手牵羊',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.diamond,
        'number': 3,
    },
    {
        'name': '顺手牵羊',
        'type': Type.dismantle,
        'category': Category.tip,
        'suit': Suit.diamond,
        'number': 4,
    },
    {
        'name': '无中生有',
        'type': Type.more,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 7,
    },
    {
        'name': '无中生有',
        'type': Type.more,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 8,
    },
    {
        'name': '无中生有',
        'type': Type.more,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 9,
    },
    {
        'name': '无中生有',
        'type': Type.more,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 11,
    },
    {
        'name': '借刀杀人',
        'type': Type.borrow,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 12,
    },
    {
        'name': '借刀杀人',
        'type': Type.borrow,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 13,
    },
    {
        'name': '无懈可击',
        'type': Type.imok,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 11,
    },
    {
        'name': '无懈可击',
        'type': Type.imok,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 12,
    },
    {
        'name': '无懈可击',
        'type': Type.imok,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 13,
    },
    {
        'name': '南蛮入侵',
        'type': Type.allkill,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 7,
    },
    {
        'name': '南蛮入侵',
        'type': Type.allkill,
        'category': Category.tip,
        'suit': Suit.spade,
        'number': 13,
    },
    {
        'name': '南蛮入侵',
        'type': Type.allkill,
        'category': Category.tip,
        'suit': Suit.club,
        'number': 13,
    },
    {
        'name': '万箭齐发',
        'type': Type.alldodge,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 1,
    },
    {
        'name': '桃园结义',
        'type': Type.allheal,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 1,
    },
    {
        'name': '五谷丰登',
        'type': Type.allmore,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 3,
    },
    {
        'name': '五谷丰登',
        'type': Type.allmore,
        'category': Category.tip,
        'suit': Suit.heart,
        'number': 4,
    },
    {
        'name': '乐不思蜀',
        'type': Type.rest,
        'category': Category.delayed_tip,
        'suit': Suit.spade,
        'number': 6,
    },
    {
        'name': '乐不思蜀',
        'type': Type.rest,
        'category': Category.delayed_tip,
        'suit': Suit.heart,
        'number': 6,
    },
    {
        'name': '乐不思蜀',
        'type': Type.rest,
        'category': Category.delayed_tip,
        'suit': Suit.club,
        'number': 6,
    },
    {
        'name': '闪电',
        'type': Type.thunder,
        'category': Category.delayed_tip,
        'suit': Suit.spade,
        'number': 1,
    },
    {
        'name': '诸葛连弩',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.club,
        'number': 1,
    },
    {
        'name': '诸葛连弩',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.diamond,
        'number': 1,
    },
    {
        'name': '八卦阵',
        'type': Type.shield,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 2,
    },
    {
        'name': '八卦阵',
        'type': Type.shield,
        'category': Category.equipment,
        'suit': Suit.club,
        'number': 2,
    },
    {
        'name': '雌雄双股剑',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 2,
    },
    {
        'name': '青龙偃月刀',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 5,
    },
    {
        'name': '绝影',
        'type': Type.defense_horse,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 5,
    },
    {
        'name': '的卢',
        'type': Type.defense_horse,
        'category': Category.equipment,
        'suit': Suit.club,
        'number': 5,
    },
    {
        'name': '青釭剑',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 6,
    },
    {
        'name': '丈八蛇矛',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 12,
    },
    {
        'name': '大宛',
        'type': Type.attack_horse,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 13,
    },
    {
        'name': '麒麟弓',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.heart,
        'number': 5,
    },
    {
        'name': '赤兔',
        'type': Type.attack_horse,
        'category': Category.equipment,
        'suit': Suit.heart,
        'number': 5,
    },
    {
        'name': '贯石斧',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.diamond,
        'number': 5,
    },
    {
        'name': '方天画戟',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.diamond,
        'number': 12,
    },
    {
        'name': '爪黄飞电',
        'type': Type.defense_horse,
        'category': Category.equipment,
        'suit': Suit.heart,
        'number': 13,
    },
    {
        'name': '紫骍',
        'type': Type.attack_horse,
        'category': Category.equipment,
        'suit': Suit.diamond,
        'number': 13,
    },
]

ex_package = [
    {
        'name': '无懈可击',
        'type': Type.imok,
        'category': Category.tip,
        'suit': Suit.diamond,
        'number': 12,
    },
    {
        'name': '闪电',
        'type': Type.thunder,
        'category': Category.delayed_tip,
        'suit': Suit.heart,
        'number': 12,
    },
    {
        'name': '寒冰剑',
        'type': Type.weapon,
        'category': Category.equipment,
        'suit': Suit.spade,
        'number': 2,
    },
    {
        'name': '仁王盾',
        'type': Type.shield,
        'category': Category.equipment,
        'suit': Suit.club,
        'number': 2,
    },
]

raw_cards = {
    Package.standard: standard_package,
    Package.ex: ex_package,
}
