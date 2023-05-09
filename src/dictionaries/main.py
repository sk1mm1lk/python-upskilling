#!/usr/bin/env python

def main():
    # Example of initialising a dictionary and printing out the key-value pair
    dict_example_1 = {
            "my_key": "my_value",
            "another_kay": "another_value",
            "year": 2023
            }

    # One way of iterating through a dictionary
    print("Example 1")
    for element in dict_example_1:
        print(element, end=" --> ")
        print(dict_example_1[element])

    # Another example of initialising a dictionary and printing out the key-value pair
    dict_example_2 = dict(my_key="my_value", name="David", age=101, year=2023)

    # Another way of iterating through a dictionary
    print("\nExample 2")
    for key, value in dict_example_2.items(): # Each element will be a tuple
        print('{} --> {}'.format(key, value))

    # An example of adding a key to the dictionary
    dict_example_3 = {
            "my_key": "my_value",
            "another_kay": "another_value",
            "year": 2023
            }

    print("\nExample 3")
    print(dict_example_3)

    # Adding a key-value pair to the dictionary
    dict_example_3["yet_another_key"] = "yet_another_value"

    print(dict_example_3)

if __name__ == "__main__":
    main()
