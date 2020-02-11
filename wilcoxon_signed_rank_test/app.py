import argparse

from wilcoxon_signed_rank_test.load_data import load_data
from wilcoxon_signed_rank_test.process_data import test_statistic, permutation, weighting
from wilcoxon_signed_rank_test.save_data import save_data


def run():
    parser = argparse.ArgumentParser(description='run options')
    parser.add_argument('--data_path', help='path to xls data file')
    parser.add_argument('--out_path', help='path to csv out file')
    parser.add_argument('--key_product_idx', type=int, help='index of column with key product')

    args = parser.parse_args()
    print(f'args: {args}')

    names, data = load_data(args.data_path)
    product_key = names[args.key_product_idx]
    non_key_products = names[args.key_product_idx + 1:]

    print(f'product_key: {product_key}, non_key_products: {non_key_products} ')
    print(f'rows in data: {len(data)}')

    for idx, row in enumerate(non_key_products, start=args.key_product_idx + 1):
        test_statistic_res = test_statistic(data, args.key_product_idx, idx)
        print(f'test statistic between {product_key} and {row} equal {abs(test_statistic_res)}')

    permutation_columns, result = permutation(data, non_key_products, args.key_product_idx + 1)
    weighting_columns, result = weighting(result, non_key_products, args.key_product_idx + 1)

    save_data(result, list(names) + permutation_columns + weighting_columns, args.out_path)

    return 0

