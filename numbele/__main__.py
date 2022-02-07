from sys import stdin
from numbele.numbele import Numbele


def get_color_squares(answer_check_list):
    color_squares = [None] * len(answer_check_list)
    for index, n in enumerate(answer_check_list):
        if n == 0:
            color_squares[index] = '⬛'
        elif n == 1:
            color_squares[index] = '🟩'
        elif n == 2:
            color_squares[index] = '🟨'
    return color_squares


def is_int(s):
    try:
        int(s, 10)
    except ValueError:
        return False
    return True


def main():
    print('Input number of answer\'s number of digits '
        + '(if input other chars means 5) : ', end='', flush=True)
    s = stdin.readline().rstrip()
    number_of_digits = 5 if not is_int(s) else int(s)
    numbele = Numbele(number_of_digits, False)
    print('Let\'s start the game!')

    while (True):
        print('Input ' + str(number_of_digits)
            + ' numbers you expect : ', end='', flush=True)
        expect_num = stdin.readline().rstrip()
        if not is_int(expect_num) or len(expect_num) != number_of_digits:
            continue

        numbele.check_number(expect_num)

        color_squares = ''.join(get_color_squares(numbele.answer_check_list))
        print(color_squares, flush=True)
        if color_squares.count('🟩') == number_of_digits:
            break

    print('Congratulations!\nAnswer number is ' + numbele.answer_num,
        flush=True)


if __name__ == '__main__':
    main()
