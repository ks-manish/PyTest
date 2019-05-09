'''Python script for creating pyramind based on input number'''
import argparse


class Pyramind(object):

    '''Function to create pyramind for given number'''
    @staticmethod
    def pyramind_full(n):
        for x in range(1, 2*n):
            #print(x)
            for y in range(1, 2*n):
                if x <= n:
                    if x+y > n and x+y < n+2*x:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    if x-y < n and x+y < n*3:
                        print("*", end="")
                    else:
                        print(" ", end="")
            print("\n")

    @staticmethod
    def pyramind(n):
        for x in range(1, n+1):
            #print(x)
            for y in range(1, 2*n):
                if x+y > n and x+y < n+2*x:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("\n")


    @staticmethod
    def half_pyramind_right(n):
        for x in range(n):
            for y in range(n):
                if x+y >= n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("\n")

    @staticmethod
    def half_pyramind_left(n):
        for x in range(n):
            for y in range(n):
                if x>=y:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("\n")

    @staticmethod
    def half_pyramind_right_down(n):
        for x in range(n):
            for y in range(n):
                if x+y > n-1:
                    print(" ", end="")
                else:
                    print("*", end="")
            print("\n")

    @staticmethod
    def half_pyramind_left_down(n):
        for x in range(n):
            for y in range(n):
                if x>y:
                    print(" ", end="")
                else:
                    print("*", end="")
            print("\n")


class Sort(object):

    '''Class for sorting algorithms'''
    def merge_sort(self, unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list
        middle = len(unsorted_list)//2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)
        return self.merge(left_list, right_list)

    @staticmethod
    def merge(left_half, right_half):
        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res



    @staticmethod
    def bubble_sort(unsorted_list, reverse=False):
        for x in range(len(unsorted_list)-1):
            temp = 0
            for y in range(x+1, len(unsorted_list)):
                if reverse:
                    if unsorted_list[x] < unsorted_list[y]:
                        temp = unsorted_list[x]
                        unsorted_list[x] = unsorted_list[y]
                        unsorted_list[y] = temp
                else:
                    if unsorted_list[x] > unsorted_list[y]:
                        temp = unsorted_list[x]
                        unsorted_list[x] = unsorted_list[y]
                        unsorted_list[y] = temp
        #return unsorted_list
        print(unsorted_list)

    @staticmethod
    def insertion_sort(InputList):
        for i in range(1, len(InputList)):
            j = i-1
            nxt_element = InputList[i]
            # Compare the current element with next one

            while (InputList[j] > nxt_element) and (j >= 0):
                InputList[j+1] = InputList[j]
                #print(InputList)
                j=j-1
            InputList[j+1] = nxt_element
            #print(InputList)


def count_duplicate(input_list):
    dict_d = {}
    for item in input_list:
        if item in dict_d:
            dict_d[item] = dict_d[item]+1
        else:
            dict_d[item] = 1
    return dict_d

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pf', '--pyramind_full', help='Input number for full pyramind', required=True)
    parser.add_argument('-ph', '--pyramind_half', help='Input number for half pyramind', required=True)
    all_args = parser.parse_args()
    if not all_args.pyramind_full or not all_args.pyramind_half:
        logging.info("invalid parameter!")
        exit()
    obj =  Pyramind()
    obj.pyramind_full(int(all_args.pyramind_full))
    obj.pyramind(int(all_args.pyramind_half))
