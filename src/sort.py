# -*- coding: utf-8 -*-


def create(config_dict):
    if config_dict['type'] == 'bubble':
        lower = config_dict['lower']
        return BubbleSort(lower)
    elif config_dict['type'] == 'select':
        lower = config_dict['lower']
        return SelectSort(lower)
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
        if lower:
            self.__check = lambda a, b: True if a <= b else False
        else:
            self.__check = lambda a, b: True if a > b else False

    def sort(self, data):
        u"""
        ソートする

        Args:
            data: データ(list of value)

        Returns:
            True: 完了
            False: まだやれる
        """

        swapped = False
        for i in range(len(data) - 1):
            if self.__check(data[i], data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        return not swapped


class SelectSort:
    def __init__(self, lower):
        self.__index = 0
        if lower:
            self.__get_id = lambda data: max(
                    range(self.__index, len(data)), key=data.__getitem__)
        else:
            self.__get_id = lambda data: min(
                    range(self.__index, len(data)), key=data.__getitem__)



    def sort(self, data):
        target_index = self.__get_id(data)
        data[self.__index], data[target_index] = data[target_index], data[self.__index]
        self.__index += 1
        if self.__index == len(data):
            return True
        return False
