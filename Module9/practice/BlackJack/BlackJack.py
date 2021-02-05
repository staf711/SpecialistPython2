# from cards import Deck, Card
import json
from classes.Deck import BJDeck
# json.loads()

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки
def count_point(cards,points):
    for card in cards:
        points += card.point
    return points
deck = BJDeck()
deck.shuffle()
while True:
    player_point = 0
    rate_point = 0
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    if player_cards == []: break
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(player_cards)
    print(dealer_cards)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    player_point=count_point(cards=player_cards,points=player_point)
    if player_point == 21:
        print("This is Black Jack!!!")
        player_money += rate_value * 1.5
        break
    # # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще/достаточно: ")
        if player_choice.lower() == "еще" or player_choice.lower() == "ещё":
            player_cards+=deck.draw(1)
            print(player_cards)
            player_point=count_point(cards=player_cards,points=player_point)
            if player_point == 21:
                print("This is Black Jack!!!")
                player_money += rate_value * 1.5
                break
            elif player_point > 21:
                print("Перебор :(")
                break
            # Раздаем еще одну карту
            # Если перебор (>21), заканчиваем добор
            ...
        if player_choice.lower() == "достаточно":
            dealer_cards+=deck.draw(1)
            rate_point=count_point(cards=dealer_cards,points=rate_point)
            if player_point == 21:
                print("This is Black Jack!!!")
                player_money += rate_value * 1.5
                break
            # Заканчиваем добирать карты

            break

    # # Если у игрока не 21(блэкджек) и нет перебора, то
    # while True:  # дилер начинает набирать карты.
    #     ...  # Смотри подробные правила добора дилера в задании
    #
    # # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
