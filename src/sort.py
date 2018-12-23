# -*- coding: utf-8 -*-


def create(config_dict):
    if config_dict['type'] == 'bubble':
        lower = config_dict['lower']
        return BubbleSort(lower)
    else:
        raise NotImplementedError(
                '{} is not implemented'.format(config_dict['type']))


class BubbleSort:
    u"""
    バブルソートを行う
    隣り合う2つの要素を比較して、指定された大小関係でないなら入れ替える
    """
    def __init__(self, lower):
        u"""
        Args:
            lower: 降順にする(bool)
        """
        self.__lower = lower

    def sort(self, data):
        u"""
        ソートする

        Args:
            data: データ(list of value)

        Returns:
            True: 完了
            False: まだやれる
        """
        if self.__lower:
            check = lambda a, b: True if a <= b else False
        else:
            check = lambda a, b: True if a > b else False

        for i in range(len(data) - 1):
            if check(data[i], data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                return False

        return True

