def chease_and_crackers(chease_count, box_crackers):
    print("you have %d chease" % chease_count)
    print("you have %d crackers" % box_crackers)


print("we can just give function number directly")
chease_and_crackers(200, 300)

print("or we can use variables from the list")
amount_of_chease = 600
amount_of_crackers = 700

chease_and_crackers(amount_of_chease, amount_of_crackers)

print("we can also do math inside")

chease_and_crackers(10 + 30, 98 + 65)

print("combining two variables and math")

chease_and_crackers(amount_of_chease + 300, amount_of_crackers + 98)
