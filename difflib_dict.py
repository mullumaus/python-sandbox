#!/usr/bin/env python3

from difflib import SequenceMatcher
from difflib import get_close_matches


if __name__ == "__main__":
    check = SequenceMatcher(None, "chinna", "china")
    print(check.ratio())

    print(get_close_matches("chinnna", ["china", "france", "india", "usa"]))

    #
    population_dict = {
        "china": 1439,
        "india": 1380,
        "usa": 331,
        "france": 65,
        "germany": 83,
        "spain": 46,
    }
    while True:
        country_name = input("Please enter country name(type exit to close)").lower()
        if country_name == "exit":
            break

        if country_name in population_dict.keys():
            print(population_dict[country_name])
        else:
            maybe_country = get_close_matches(country_name, population_dict.keys())
            if maybe_country == []:
                print(
                    f"Please check the input country name. \
                        Data is not available for {country_name}"
                )
            else:
                ans = input("Do you mean %s type y or n." % maybe_country[0])
                if ans == "y":
                    print(population_dict[maybe_country[0]])
                else:
                    print("Bad input, try again")
