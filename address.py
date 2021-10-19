#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: October 2021
# This program gets info from user and shows their address


def address_formatted(
    full_name, street_num, street_name, city, province, postal_code, apt_number=None
):
    # return the full formal name

    formatted = full_name
    if apt_number is not None:
        formatted = "{0} \n{1} - {2} {3} \n{4} {5}  {6}".format(
            full_name,
            apt_number,
            street_num,
            street_name,
            city,
            province,
            postal_code,
        )
    else:
        formatted = "{0} \n{1} {2} \n{3} {4}  {5} ".format(
            full_name,
            street_num,
            street_name,
            city,
            province,
            postal_code,
        )

    return formatted


def main():
    # gets users info to format to send package
    apt_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartement? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    street_num = input("Enter your street number: ")
    street_name = input("Enter your street name AND type (Main St...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (short form): ")
    postal_code = input("Enter your postal code: ")

    if apt_number is not None:
        card = address_formatted(
            full_name, street_num, street_name, city, province, postal_code, apt_number
        )
    else:
        card = address_formatted(
            full_name, street_num, street_name, city, province, postal_code
        )

    card_up = card.upper()

    print("\n")
    print(card_up)
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
