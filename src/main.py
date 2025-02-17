import argparse

def align():
    parser = argparse.ArgumentParser(description="Aligns images based on a template.")
    parser.add_argument('template', help='Path to the template image file')
    parser.add_argument('input_dir', help='Path to a folder containing the images to be aligned.')
    args = parser.parse_args
    print('works')