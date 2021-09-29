import argparse

def get_cli_args() -> (str, int):
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", default='', help="path to video file")
    ap.add_argument("-a", "--area", default=500, help="minimum area size")
    args = vars(ap.parse_args())

    return (args['input'], args['area'])

