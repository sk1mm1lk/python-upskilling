#!/usr/bin/env python

def main():
    # Example of creating and iterating through a set
    print("Example 1")
    set_example_1 = { "David", True, 7 }

    for element in set_example_1:
        print(str(element))

    # Another example of creating a set
    print("\nExample 2")
    set_example_2 = set(("David", True, 7))

    for element in set_example_2:
        print(str(element))

    # An example of adding to a set
    print("\nExample 3")
    set_example_3 = set(("David", True, 7))

    for element in set_example_3:
        print(str(element))

    set_example_3.add(False)
    print("----------")

    for element in set_example_3:
        print(str(element))


if __name__ == "__main__":
    main()
