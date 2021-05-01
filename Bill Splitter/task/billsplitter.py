# write your code here
import random


def main():
    n_people = int(input("Enter the number of friends joining (including you):"))
    print()
    if n_people <= 0:
        print("No one is joining for the party")
        return
    print("Enter the name of every friend (including you), each on a new line:")
    guests = {}

    for i in range(n_people):
        guests.update({input(): 0})
    print()
    total_bill = int(input("Enter the total bill value:"))
    print()
    who_is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    if who_is_lucky == "Yes":
        lucky_one = random.sample(guests.keys(), k=1)
        print(f"{lucky_one[0]} is the lucky one!")
    else:
        lucky_one = ""
        print("No one is going to be lucky")

    for key in guests.keys():
        if who_is_lucky != "Yes":
            guests.update({key: round(total_bill / n_people, ndigits=2)})
        else:
            if key != lucky_one[0]:
                guests.update({key: round(total_bill / (n_people - 1), ndigits=2)})

    print()
    print(guests)


main()
