import argparse

from wilcoxon_signed_rank_test.data.load_data import load_data


def run():
    parser = argparse.ArgumentParser(description='run options')
    parser.add_argument('--data_path', help='path to xls file')

    args = parser.parse_args()
    print(args)

    data = load_data(args.data_path)
    return data

