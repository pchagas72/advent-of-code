#!/usr/bin/env python3

from dict import huge_d
import time
import threading

values_dic = huge_d.values_dic

class solve():

    def __init__(self):
        pass

    def read_file(self, filename):
        with open(filename, 'r') as f:
            values = f.readlines()
            return values

    def divide_sacks(self,data):
        sacks_divided = []
        for sack in data:
            sack = sack.replace("\n", "")
            total_l = len(sack)
            l = total_l/2
            comp1 = []
            comp2 = []
            for i in range(total_l):
                if i <= l-1:
                    comp1.append(sack[i])
                elif i > l-1:
                    comp2.append(sack[i])
                    divided = (comp1, comp2)
                    sacks_divided.append(divided)
        return sacks_divided

    def divide_equals(self,divided_data):
        equals = []
        for i in divided_data:
            es = i[0]
            di = i[1]
            common_list = [c for c in es if c in di]
            common = common_list[0]
            equals.append(common)
        return equals

    def divide_groups(self, data):
            groups_divided = []
            counter = 0
            gs1 = []
            gs2 = []
            gs3 = []
            for group in data:
                group = group.replace("\n", "")
                if counter == 0:
                    gs1.append(group)
                    counter += 1
                elif counter == 1:
                    gs2.append(group)
                    counter += 1
                elif counter == 2:
                    gs3.append(group)
                    counter = 0
            return (gs1, gs2, gs3)

    def organize_groups(self, divided_data): #It's 3:23 AM and I want to sleep
            gst = []
            gs1, gs2, gs3 = divided_data
            lt = len(gs1)
            for i in range(lt):
                appnd = (gs1[i], gs2[i], gs3[i])
                gst.append(appnd)
            return gst

    def get_common_values(self, organized_data):
            cv = []
            for i in organized_data:
                f = set(i[0])
                s = set(i[1])
                t = set(i[2])
                commons = list(f & s & t)
                common = commons[0]
                cv.append(common)
            return cv

    def sum_values(self, values, dic):
            sums = 0
            for i in values:
                sums += dic[i]
            return sums

    def print_answers(self):

        # First processing
        d_sacks = self.divide_sacks(self, self.read_file(self, "input.txt"))
        equals = self.divide_equals(self, d_sacks)
        sum_equals = self.sum_values(self, equals, values_dic)
        # Second processing
        d_groups = self.divide_groups(self, self.read_file(self, "input.txt"))
        o_groups = self.organize_groups(self, d_groups)
        common_values = self.get_common_values(self, o_groups)
        v_sum = self.sum_values(self, common_values, values_dic)
        # Printing
        print(f"The second answer is {v_sum}")
        print(f"The first answer is {sum_equals}")
