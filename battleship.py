import random


def create_random_ship():
    return random.randint(0, 6), random.randint(0, 6)


def play_again():
    try_again = input("Хочешь поиграть еще раз? <Д>а or <Н>ет? >: ").lower()
    if try_again == "Д":
        play_game()
    else:
        print("Пока!!!")
        return


print("Добро пожаловать в игру Морской бой"
      "\nВаша главная цель - найти и уничтожить все спрятанные корабли на карте!\n")

print("""\nИнструкции:
\nУ вас есть 10 патронов, и на карте есть 3 скрытых корабля.
Чтобы поразить их, вы должны ввести определенные цифры для этого местоположения. Например:
Для первой строки и первого столбца вы должны написать 1 и 1.
Я желаю вам удачи в грядущих войнах!\n""")


def play_game():
    game_board = [["O", "O", "O", "O", "O", "0"],
                  ["O", "O", "O", "O", "O", "0"],
                  ["O", "O", "O", "O", "O", "0"],
                  ["O", "O", "O", "O", "O", "0"],
                  ["O", "O", "O", "O", "O", "0"],
                  ["0", "O", "O", "O", "O", "0"]]

    for i in game_board:
        print(*i)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ships_left = 3
    ammo = 10

    while ammo:
        try:
            row = int(input("Введите номер строки между 1-6 >: "))
            column = int(input("Введите номер столбца между 1-6 >: "))
        except ValueError:
            print("Вводите только номер!")
            continue

        if row not in range(1,7) or column not in range(1, 7):
            print("\nЧисла должны быть в диапазоне от 1 до 6!")
            continue

        row = row - 1
        column = column - 1

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nВы уже снимали это место!\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("\nБум! Вы попали! Корабль взорвался! Вам выдали новые боеприпасы!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("Боже мой, я и не знал, что ты такой меткий стрелок! Поздравляю, ты победил")
                play_again()
        else:
            print("\nТы промахнулся!\n")
            game_board[row][column] = "-"
            ammo -= 1

        for i in game_board:
            print(*i)

        print(f"Патронов осталось: {ammo} | Кораблей осталось: {ships_left}")

    play_again()


if __name__ == "__main__":
    play_game()