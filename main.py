#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This programs adds 2 numbers


def main():
    # This function input 2 numbers and output sum

    # input
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    # process
    process = first + second

    # output
    print(f"{first} + {second} = {process}")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
