#!/usr/bin/python3
"""Module contains a function
that returns the Pascals triangle"""


def pascal_triangle(n):
    """This function contains the function implementation"""
    if (n <= 0):
        return ([])
    main_list = [[1]]
    for i in range(0, (n - 1)):
        sub_list = [1]
        for j in range(0, i):
            sub_list.append(main_list[i][j] + main_list[i][j + 1])
        sub_list.append(1)
        main_list.append(sub_list)
    return (main_list)


if __name__ == "__main__":
    for row in pascal_triangle(5):
        print("[{}]".format(",".join([str(x) for x in row])))
