import argparse


def process_arguments(args):
    print("Nom:", args.name)
    print("Age:", args.age)
    print("Ville:", args.city)


parser = argparse.ArgumentParser()

parser.add_argument('-n', '--name', type=str, help="Votre nom")
parser.add_argument('-a', '--age', type=int, help="Votre age")
parser.add_argument('-c', '--city', type=str, help="Votre ville")

args = parser.parse_args()

process_arguments(args)

