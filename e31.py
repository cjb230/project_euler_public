import datetime

COINS = (1, 2, 5, 10, 20, 50, 100, 200)


def get_ways(target, max_coin):
    if target < 2:
        return 1
    if max_coin == 1:
        return 1
    if max_coin > target:
        return get_ways(target, next_lower_coin(max_coin))
    else:
        total_ways = get_ways(target, next_lower_coin(max_coin))
        max_coin_instances = 1
        while max_coin_instances * max_coin <= target:
            total_ways += get_ways(target - (max_coin_instances * max_coin), next_lower_coin(max_coin))
            max_coin_instances += 1
        return total_ways


def next_lower_coin(this_coin):
    return_val = None
    if this_coin == 2:
        return_val = 1
    elif this_coin == 5:
        return_val = 2
    elif this_coin == 10:
        return_val = 5
    elif this_coin == 20:
        return_val = 10
    elif this_coin == 50:
        return_val = 20
    elif this_coin == 100:
        return_val = 50
    elif this_coin == 200:
        return_val = 100
    else:
        print("Bad coin value:" + str(this_coin))
        exit()
    return return_val


if __name__ == "__main__":
    start = datetime.datetime.now()
    print(get_ways(200, 200))
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
