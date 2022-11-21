# coding: utf-8

from func import const, mouse, button

const.MAX_STICKY = 8


class Sticky():
    id = 0
    text = ""
    right = 0
    bottom = 0
    width = 0
    height = 0


def Format():
        one = Sticky()
        one.id = 1
        one.right = 80
        one.bottom = 80
        one.width = 30
        one.height = 20

        two = Sticky()
        two.id = 2
        two.right = 100
        two.bottom = 10
        two.width = 40
        two.height = 40

        three = Sticky()
        three.id = 3
        three.right = 50
        three.bottom = 20
        three.width = 30
        three.height = 50

        four = Sticky()
        four.id = 4
        four.right = 20
        four.bottom = 60
        four.width = 40
        four.height = 30

        five = Sticky()
        five.id = 5
        five.right = 90
        five.bottom = 80
        five.width = 40
        five.height = 10

