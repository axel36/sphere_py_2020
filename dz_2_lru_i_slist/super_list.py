"""custom list"""
import copy


def get_small_and_big(first, second):
    """check length of lists"""
    first_is_big = len(first) > len(second)
    if first_is_big:
        return second, first
    return first, second


class SuperList(list):
    """super puper list"""

    def __add__(self, other):
        small, big = get_small_and_big(self, other)
        ret = copy.deepcopy(big)

        for i, elem in enumerate(small):
            ret[i] = elem + ret[i]

        return ret

    def __sub__(self, other):
        neg_other = [-x for x in other]
        return self.__add__(neg_other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)
