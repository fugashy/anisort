# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import matplotlib.animation as animation


class OncePlotter:
    u"""
    シンプルな描画クラス
    画面更新後、すぐに制御を返す
    """
    def __init__(self, label=('x', 'y')):
        u"""
        Args:
            name: ウィンドウ名(str)
            label: ラベル名(tuple of str)
        """
        plt.xlabel(label[0])
        plt.xlabel(label[0])

    def plot_once(self, data):
        u"""
        データを描画する

        Args:
            data: データ(list of value)
        """
        plt.plot(data)
        plt.pause(0.01)
