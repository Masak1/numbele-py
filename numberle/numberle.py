import datetime
import random

"""
数字はstringで管理する
=== self.answer_check_listについて ======
    0 : 数字の存在が不正解
    1 : 数字も位置も正解
    2 : 数字は存在するが位置が不正解
"""
class Numberle:

    def __init__(self, number_of_digits, is_use_random_seed):
        self.number_of_digits = number_of_digits
        self.answer_num = self.generate_answer_num(is_use_random_seed)
        self.answer_check_list = self.init_answer_check_list()

    def generate_answer_num(self, is_use_random_seed):
        if not is_use_random_seed:
            d_today = datetime.date.today()
            d_today_int = int(d_today.strftime('%y%m%d'))
            random.seed(d_today_int)
        return (str(int(random.uniform(0, 10 ** self.number_of_digits - 0.5)))
            .zfill(self.number_of_digits))

    def init_answer_check_list(self):
        self.answer_check_list = [0] * self.number_of_digits

    def check_number(self, expect_num):
        self.init_answer_check_list()

        for i in range(self.number_of_digits):
            if expect_num[i] == self.answer_num[i]:
                self.answer_check_list[i] = 1
                continue
            self.answer_check_list[i] = 0

        match_index_num = [[i, self.answer_num[i]]
            for i in range(self.number_of_digits)
            if self.answer_check_list[i] == 1]
        
        for i in range(self.number_of_digits):
            if expect_num[i] == self.answer_num[i]:
                self.answer_check_list[i] = 1
                continue
            elif expect_num[i] in self.answer_num[:i]:
                num_in_left_of_expect = expect_num[:i].count(expect_num[i])
                match_in_left_num  = len([j for j in match_index_num
                    if j[1] == expect_num[i] and j[0] < i])
                match_in_right_num = len([j for j in match_index_num
                    if j[1] == expect_num[i] and j[0] > i])
                used_in_ans = self.answer_num.count(expect_num[i])

                if (num_in_left_of_expect >= match_in_left_num
                    and match_in_left_num >= 1
                    or match_in_right_num + num_in_left_of_expect
                    >= used_in_ans):
                    continue
                self.answer_check_list[i] = 2
            elif expect_num[i] in self.answer_num[i + 1:]:
                num_in_left_of_expect = expect_num[:i].count(expect_num[i])
                match_in_right_num = len([j for j in match_index_num
                    if j[1] == expect_num[i] and j[0] > i])
                used_in_ans = self.answer_num.count(expect_num[i])
                
                if (match_in_right_num == used_in_ans
                    and match_in_right_num >= 1
                    or num_in_left_of_expect >= used_in_ans):
                    continue
                self.answer_check_list[i] = 2

        return self.answer_check_list
