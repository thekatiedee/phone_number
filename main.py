def phone_num():

    count = 0
    the_list = []
    while count < 10:
        # ask for input to add a number, one by one
        num = int(input("pick a number: "))
        # increase count after testing that the number is indeed between 0-9
        # add line about not dialing 0 first
        if num >= 0 and num <= 9:
            count += 1
            the_list.append(num)
        # if below 0, or above 9, prompt for a new number. count doesn't increase.
        else:
            print("sorry! pick something between 0 and 9!")
    # break apart the list into three smaller lists
    first = the_list[0:3]
    second = the_list[3:6]
    third = the_list[6:10]
    # turn individual lists into strings
    first_string = "".join(str(x) for x in first)
    second_string = "".join(str(x) for x in second)
    third_string = "".join(str(x) for x in third)
    # combine the strings with a hyphen
    combined = f"{first_string}-{second_string}-{third_string}"
    print("your phone number is: ", combined)


if __name__ == "__main__":
    phone_num()
