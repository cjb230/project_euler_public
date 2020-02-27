import datetime
import math
n = 1001

PARTITION_RESULTS = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15}
PARTITION_LIMITED_RESULTS = [[0] * (n - 1) for i in range (1, n)]


def calculate_partition_result(partition_input):
    if partition_input < 3:
        print("calculate_partition_result(" + str(partition_input) + "): value too small")
        return
    result = 2 # for the two results guaranteed to be  present: all 1s, and "partition_input" by itself
    for largest_summand in range(partition_input - 1, 1, -1):
        max_summand_multiple = math.floor(partition_input / largest_summand)
        for summand_multiple in range(max_summand_multiple, 0, -1):
            partition_remainder = partition_input - (summand_multiple * largest_summand)
            if partition_remainder == 0:
                result += 1
            else:
                subpartition_summand_limit = min(largest_summand - 1, partition_remainder)
                if subpartition_summand_limit == 1:
                    result += 1
                else:
                    result += get_subpartition_result(partition_remainder, subpartition_summand_limit)
    return result


def calculate_subpartition_result(partition, summand_limit):
    if summand_limit == 1:
        return 1
    result = 0
    max_summand_multiple = math.floor(partition / summand_limit)
    for summand_multiple in range(max_summand_multiple, 0, -1):
        remaining_partition = partition - (summand_multiple * summand_limit)
        if remaining_partition == 0:
            result += 1
        else:
            remaining_summand = min(remaining_partition, summand_limit - 1)
            result += get_subpartition_result(remaining_partition, remaining_summand)
    if summand_limit > 0:
        result += get_subpartition_result(partition, summand_limit - 1)
    return result


def get_partition_result(partition_input):
    global PARTITION_RESULTS
    current_max = len(PARTITION_RESULTS)
    if partition_input > current_max:
        for i in range(current_max + 1, partition_input + 1):
            PARTITION_RESULTS[i] = calculate_partition_result(i)
    return PARTITION_RESULTS[partition_input]


def get_subpartition_result(partition, summand_limit):
    global PARTITION_LIMITED_RESULTS
    if summand_limit < 1:
        print("get_subpartition_result(" + str(partition) + ", " + str(summand_limit) + "): summand_limit too small")
        return
    elif partition < 1:
        print("get_subpartition_result(" + str(partition) + ", " + str(summand_limit) + "): partition too small")
        return
    elif partition < summand_limit:
        print("get_subpartition_result(" + str(partition) + ", " + str(summand_limit) + "): partition < summand_limit")
        return
    elif partition == summand_limit:
        return get_partition_result(partition)
    elif PARTITION_LIMITED_RESULTS[partition - 1][summand_limit - 1] == 0:
        PARTITION_LIMITED_RESULTS[partition - 1][summand_limit - 1] = calculate_subpartition_result(partition, summand_limit)
    return PARTITION_LIMITED_RESULTS[partition - 1][summand_limit - 1]


if __name__ == "__main__":
    start = datetime.datetime.now()
    print(get_partition_result(1000) - 1)
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
