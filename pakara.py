#カード解除作成

# プレイヤーとバンカーを交互にカードを配布(計2枚)

import random
mark = ["♤ ", "♧ ", "♡ ", "♢ "]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_deck = []
player_card = []
cpu_card = []

def card_master():
    for mark_idx in range(4):
        for number_idx in range(13):
            card_deck.append(number[number_idx])

def player(maisu):
    player_card.extend(random.sample(card_deck, maisu))
    for idx in range(maisu):
        card_deck.remove(player_card[idx])

def cpu(maisu):
    cpu_card.extend(random.sample(card_deck, maisu))
    for idx in range(maisu):
        card_deck.remove(cpu_card[idx])

def player_card_add():
    global player_card
    player_card = [i for i in player_card if i < 10]
    player_card_sum = sum(player_card)
    str_player_card_sum = str(player_card_sum)
    str_player_card_sum1 = str_player_card_sum[-1]

def cpu_card_add():
    global cpu_card
    cpu_card = [i for i in cpu_card if i < 10]
    cpu_card_sum = sum(cpu_card)
    str_cpu_card_sum = str(cpu_card_sum)
    str_cpu_card_sum1 = str_cpu_card_sum[-1]

card_master()
player(2)
cpu(2)

#10~13を削除、カードの合計処理
player_card = [i for i in player_card if i < 10]
cpu_card = [i for i in cpu_card if i < 10]

#カードの合計処理
player_card_sum = sum(player_card)
cpu_card_sum = sum(cpu_card)
str_player_card_sum = str(player_card_sum)
str_cpu_card_sum = str(cpu_card_sum)
str_player_card_sum1 = str_player_card_sum[-1]
str_cpu_card_sum1 = str_cpu_card_sum[-1]

#プレイヤーが0~5の場合カードを一枚引く
if int(str_player_card_sum1) <= 5:
    player(1)
    player_card_3maime = player_card[-1]
    player_card_add()

    #バンカーのカードが0~2の場合カードを一枚引く
    if int(str_cpu_card_sum1) <= 2:
        cpu(1)
        cpu_card_add()

    #バンカーのカードが3でプレイヤーの3枚目が8以外の場合カードを一枚引く
    elif int(str_cpu_card_sum1) == 3 and player_card_3maime < 8:
        cpu(1)
        cpu_card_add()

    #バンカーのカードが4でプレイヤーの3枚目が2~7以外の場合カードを一枚引く
    elif int(str_cpu_card_sum1) == 4 and 2>= player_card_3maime <=7:
        cpu(1)
        cpu_card_add()

    #バンカーのカードが5でプレイヤーの3枚目が4,5,6,7の場合カードを一枚引く
    elif int(str_cpu_card_sum1) == 5 and 4>= player_card_3maime <=7:
        cpu(1)
        cpu_card_add()

    #バンカーのカードが6でプレイヤーの3枚目が6,7の場合カードを一枚引く
    elif int(str_cpu_card_sum1) == 6 and player_card_3maime == 6 or player_card_3maime == 7 :
        cpu(1)
        cpu_card_add()

#プレイヤーのカードが6,7の場合カードを引かない
elif int(str_player_card_sum1) <= 7:

    #バンカーが0~5の場合カードを1枚引く
    if int(str_cpu_card_sum1) <= 5:
        cpu(1)
        cpu_card_add()

#プレイヤーのカードが8,9の場合
elif int(str_player_card_sum1) <= 9:
    pass

str_player_card_sum = str(player_card_sum)
str_cpu_card_sum = str(cpu_card_sum)
str_player_card_sum1 = str_player_card_sum[-1]
str_cpu_card_sum1 = str_cpu_card_sum[-1]

#勝敗判定
if str_player_card_sum1 > str_cpu_card_sum1:
    print("プレイヤーの勝利")

elif str_player_card_sum1 < str_cpu_card_sum1:
    print("バンカーの勝利")

elif str_player_card_sum1 == str_cpu_card_sum1:
    print("タイ!")