import argparse

from wilcoxon_signed_rank_test.load_data import load_data
from wilcoxon_signed_rank_test.process_data import process_data


def run():
    parser = argparse.ArgumentParser(description='run options')
    parser.add_argument('--data_path', help='path to xls file')
    parser.add_argument('--key_product_idx', type=int, help='index of column with key product')

    args = parser.parse_args()
    print(f'args: {args}')

    names, data = load_data(args.data_path)
    product_key = names[args.key_product_idx]
    compare_with = names[args.key_product_idx + 1:]

    print(f'names: {names}, data[0]: {data[0]}')
    print(f'product_key: {product_key}, compare_with: {compare_with} ')

    process_data(data, args.key_product_idx, args.key_product_idx + 1)

    return 0

