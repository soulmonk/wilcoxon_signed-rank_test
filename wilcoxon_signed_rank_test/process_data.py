def sign(x):
    return x and (1, -1)[x < 0]


def rank(arr):
    result = {}
    prev_rank = 0
    for row in arr:
        if row["abs"] not in result:
            result[row["abs"]] = []
        prev_rank += 1
        result[row["abs"]].append(prev_rank)

    for key, value in result.items():
        result[key] = sum(value) / len(value)

    return result


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

    rank_data = rank(sorted_data)
    data_with_rank = list(map(lambda i: map_rank(i, rank_data), sorted_data))

    # calc test statistic W
    test_statistic = sum(item["sign_rank"] for item in data_with_rank)
    print(f'test statistic W: {test_statistic}')
    return None
