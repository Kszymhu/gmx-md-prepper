from argparse import ArgumentParser

def cli_test() -> None:
    parser = ArgumentParser()
    parser.add_argument('-m', '--message', action="store_true")
    
    args = parser.parse_args()
    print(args.message)
