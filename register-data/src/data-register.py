from azureml.core import Workspace, Dataset
import argparse


def main(args):
    path = args.data_path
    ws = Workspace.from_config()
    dataset = Dataset.Tabular.from_delimited_files(path=path)
    dataset.register(ws, 'sample-data')


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--data_path", dest='data_path',
                        type=str)

    # parse args
    args = parser.parse_args()

    # return args
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
