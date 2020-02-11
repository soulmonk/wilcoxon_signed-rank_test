import itertools


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


def map_rank(row, rank_data):
    row["rank"] = rank_data[row["abs"]]
    row["sign_rank"] = row["sign"] * row["rank"]
    return row


def test_statistic(data, product_key_idx, compare_idx):
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

    return sum(sign_ranks)


def permutation(data, columns, offset):
    hashes = {}
    permutation_column = ['permutation']

    # skip first column (will compare with)
    for idx, column in enumerate(list(columns[1:]), start=offset + 1):
        hashes[column] = {}

        for row in data:
            hashes[column][row[idx]] = 1

    result = []
    for row in data:
        perm = []
        for idx, column in enumerate(columns[1:], start=offset + 1):
            if row[offset] in hashes[column]:
                perm.append(column)
        result.append(list(row) + [",".join(perm)])

    return permutation_column, result


def weighting(data, columns, offset):

    columns_combinations = list(itertools.combinations(columns, 2))
    column_names = list(map(lambda x: "W_" + "_".join(x), columns_combinations))
    columns_indexes = {}
    for idx, column in enumerate(columns, start=offset):
        columns_indexes[column] = idx

    result = []
    for row in data:
        w = []
        for keys in columns_combinations:
            w.append((row[columns_indexes[keys[0]]] + row[columns_indexes[keys[1]]]) / 2)
        result.append(list(row) + w)

    return column_names, result
