import math


def sign(x):
    return x and (1, -1)[x < 0]


def ranks(arr):
    result = {}
    prev_idx = 0
    length = len(arr)
    for idx, row in enumerate(arr, start=1):
        if idx == length or arr[idx]["abs"] != row["abs"]:
            result[row["abs"]] = (prev_idx + 1 + idx) / 2
            prev_idx = idx
    return result


def mean(arr):
    return sum(arr) / len(arr)


def std(arr):
    return sum(arr) / len(arr)


def map_rank(row, rank_data):
    row["rank"] = rank_data[row["abs"]]
    row["sign_rank"] = row["sign"] * row["rank"]
    return row


def process_data(data, product_key_idx, compare_idx):
    data_with_sign = []

    # calculate abs and sign
    # filter remove abs == 0
    for row in data:
        x2 = int(row[product_key_idx])
        x1 = int(row[compare_idx])
        diff = x2 - x1
        if diff == 0:
            continue
        data_with_sign.append({
            "x2": x2,
            "x1": x1,
            "sign": sign(diff),
            "abs": abs(diff),
        })

    # sort by abs
    sorted_data = sorted(data_with_sign, key=lambda i: i['abs'])
    # calc rank

    rank_data = ranks(sorted_data)
    data_with_rank = list(map(lambda i: map_rank(i, rank_data), sorted_data))

    # calc test statistic W
    sign_ranks = list(item["sign_rank"] for item in data_with_rank)
    test_statistic = sum(sign_ranks)
    positive_w = sum(list((filter(lambda x: x > 0, sign_ranks))))
    negative_w = sum(list((filter(lambda x: x < 0, sign_ranks))))

    n = len(sign_ranks)
    mw = n * (n + 1) / 4
    sigw = math.sqrt((n * (n + 1) * (2 * n + 1)) / 24)

    zstat = (positive_w - mw) / sigw

    print(f'test statistic W: {test_statistic}, '
          f'positive W: {positive_w}, '
          f'negative W: {negative_w}, '
          f'n: {n}, mw: {mw}, sigw: {sigw} '
          f'z-stat: {zstat}')

    return test_statistic
