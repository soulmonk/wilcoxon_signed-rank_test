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

    print(f'product_key: {product_key}, compare_with: {compare_with} ')
    print(f'rows in data: {len(data)}')

    for idx, row in enumerate(compare_with, start=args.key_product_idx + 1):
        test_statistic = process_data(data, args.key_product_idx, idx)
        print(f'test statistic between {product_key} and {row} equal {abs(test_statistic)}')

    return 0

