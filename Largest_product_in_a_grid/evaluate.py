def evaluate(grid, item):
    print('Evaluating')
    highest_val = 0

    upPro = up(grid, item)
    if upPro > highest_val:
        highest_val = upPro

    downPro = down(grid, item)
    if downPro > highest_val:
        highest_val = downPro

    leftPro = left(grid, item)
    if leftPro > highest_val:
        highest_val = leftPro

    rightPro = right(grid, item)
    if rightPro > highest_val:
        highest_val = rightPro

    digupleftPro = dig_up_left(grid, item)
    if digupleftPro > highest_val:
        highest_val = digupleftPro

    digdownleftPro = dig_down_left(grid, item)
    if digdownleftPro > highest_val:
        highest_val = digdownleftPro

    diguprightPro = dig_up_right(grid, item)
    if diguprightPro > highest_val:
        highest_val = diguprightPro

    digdownrightPro = dig_down_right(grid, item)
    if digdownrightPro > highest_val:
        highest_val = digdownrightPro



    return highest_val


def up(grid, item):
    if grid[item]:
        if item-60 >= 0:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item - 20]) * int(grid[item - 40]) * int(grid[item - 60])
    return 0


def down(grid, item):
    if grid[item]:
        if item+60 < 400:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item + 20]) * int(grid[item + 40]) * int(grid[item + 60])
    return 0


def left(grid, item):
    if grid[item]:
        if item-3 >= 0:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item -1]) * int(grid[item -2]) * int(grid[item -3])
    return 0


def right(grid, item):
    if grid[item]:
        if item+3 < 400:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item +1]) * int(grid[item +2]) * int(grid[item +3])
    return 0


def dig_up_right(grid, item):
    if grid[item]:
        if item-57 < 400:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item -19]) * int(grid[item -38]) * int(grid[item -57])
    return 0


def dig_down_right(grid, item):
    if grid[item]:
        if item+63 < 400:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item +21]) * int(grid[item +42]) * int(grid[item +63])
    return 0


def dig_up_left(grid, item):
    if grid[item]:
        if item-63 >= 0:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item -21]) * int(grid[item -42]) * int(grid[item -63])
    return 0


def dig_down_left(grid, item):
    if grid[item]:
        if item+57 < 400:
            # return grid[item] * grid[item-20] * grid[item-40] * grid[item-60]
            return int(grid[item]) * int(grid[item +19]) * int(grid[item +38]) * int(grid[item +57])
    return 0