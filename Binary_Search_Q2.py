
def radius(houses, heaters):
    res = 0
    for house in houses:
        l = 0
        r = len(heaters) - 1
        while l < r:
            m = l + int((r - l) / 2)
            if heaters[m] == house:
                break
            elif heaters[m] < house:
                l = m + 1
            else:
                r = m
        res = max(res, min(heaters[l] - house, house - heaters[l-1]) if l > 0 else heaters[l] - house)
    return res

houses = [1,2,3]
heaters = [2]

print(radius(houses, heaters))

houses = [1,2,3,4]
heaters = [1,4]

print(radius(houses, heaters))

