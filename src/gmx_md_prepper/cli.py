from argparse import ArgumentParser

def cli_test() -> None:
    parser = ArgumentParser()
    parser.add_argument('-m', '--message', type=str)
    
    args = parser.parse_args()
    print(args.message)
