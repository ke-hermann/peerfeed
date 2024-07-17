import argparse

import database
import extract


def main():
    parser = argparse.ArgumentParser(description="A simple program to process a URL.")
    parser.add_argument(
        "-u", "--url", type=str, required=True, help="The URL to be processed."
    )

    args = parser.parse_args()

    if args.url:
        entry = extract.generate_feed_entry(args.url)
        database.insert_new_entry(entry)


if __name__ == "__main__":
    main()
