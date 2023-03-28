from argparse import ArgumentParser

def cli_main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        '-s',
        '--structure',
        type=str,
        required=True,
        help='File containing protein structure, in a format accepted by GROMACS\'s pdb2gmx.'
    )

    parser.add_argument(
        '-ff',
        '--forcefield',
        type=str,
        required=True,
        help='Directory containing your forcefield files.'
    )

    args = parser.parse_args()
    print(f'Structure file: {args.structure}')
    print(f'Forcefield: {args.forcefield}')
