#!/usr/bin/python3


def helper(n, lst):
    """helper method"""
    new_list = list(lst)
    for i in range(len(lst)):
        if lst[i] == n or lst[i] % n == 0:
            new_list.remove(lst[i])
    return new_list


def isWinner(x, nums):
    """is Winner method"""
    winner = {"Maria": 0, "Ben": 0}
    for i in range(x):
        if nums[i] == 1:
            winner["Ben"] += 1
        else:
            count = 0

            n_list = [n for n in range(2, nums[i] + 1)]  # [2,3,4,5....]

            while n_list:
                n_list = helper(n_list[0], n_list)
                count += 1

            if count % 2 == 0:
                winner["Ben"] += 1
            else:
                winner["Maria"] += 1
    if winner["Ben"] == winner["Maria"]:
        return None
    if winner["Ben"] < winner["Maria"]:
        return "Maria"
    return "Ben"
