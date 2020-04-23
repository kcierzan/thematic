#!/usr/bin/env python

import os
import pathlib


def main():
    package_dir = pathlib.Path(__file__).parent.parent.resolve()
    print(os.path.join(package_dir, "templates/themes"))


if __name__ == "__main__":
    main()
