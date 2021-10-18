#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: October 2021
# This program gets info from user and shows their address


def app_check(apartment=None):
    # return apartment

    # process
    app_live = apartment
    if apartment != None:
        app_live = app_live + " " + apartment[0]
    app_live = ""

    return app_live


def main():
    # user answers prompts and outputs mailing address
    apartment = None

    # input & output
    full = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment = input("Enter your apartment number: ")
    street_num = input("Enter your street number: ")
    street = input("Enter your street name AND type (Main St, Express Pkwy…): ")
    city = input("Enter your city name: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC): ")
    postal = input("Enter your postal code (123 456): ")

    if question.upper() == "Y" or question.upper() == "YES":
        prompt_list = app_check(apartment)
        print("\n" + full.upper())
        print(apartment + "-" + street_num.upper(), street.upper())
        print(city.upper(), province.upper(), "", postal.upper())

    else:
        prompt_list = app_check(apartment)
        print("\n" + full.upper())
        print(street_num.upper(), street.upper())
        print(city.upper(), province.upper(), "", postal.upper())

    print(prompt_list)


if __name__ == "__main__":
    main()
