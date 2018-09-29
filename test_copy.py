# get the coordinates of cards and marks
# used to get the range for function mark_crd()
# check whether the calculation is correct
# change some parameters in "card.py" "anti.py" if necessary
from init import *
from lib.ats import *
from config import *
def cards(sh):
    global quick, arts, buster
    #0.98刚好三个点
    threshold = 0.98
    quick = get_crd(sh, f'{order_card}/quick.png', threshold)
    arts = get_crd(sh, f'{order_card}/arts.png', threshold)
    buster = get_crd(sh, f'{order_card}/buster.png', threshold)

    all_cards = quick + arts + buster
    all_cards.sort()

    print("cards: ", all_cards)


def marks(sh,):
    restraint = get_restraint(sh)
    resistance = get_resistance(sh)

    print("restraint: ", restraint)
    print("resistance: ", resistance)


def test():
    # sh = screenshot()
    sh= f'{card_face}/t1.jpeg'

    cards(sh)  # show coordinates of cards
    marks(sh)  # show coordinates of marks

    print('-------------')
    print(init_main(sh))  # show the result of calculation
    print('-------------')

test()
