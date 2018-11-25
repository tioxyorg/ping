#!/usr/bin/env python
import requests
import time
import sys


def main():
    """
    Just requesting and endpoint endlessly
    """
    url = sys.argv[1]
    while True:
        r = requests.get(url)
        time.sleep(0.5)
        print(r.content)


if __name__ == "__main__":
    main()
