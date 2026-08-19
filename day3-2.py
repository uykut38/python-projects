numbers = []

while True:
    num = int(input("سان كىرگۈزۈڭ (توختاش ئۈچۈن 0): "))

    if num == 0:
        break

    numbers.append(num)

# 1. بارلىق سانلار
print("بارلىق سانلار:", numbers)

# 2. تەكرارلانمىغان سانلار
unique_numbers = set(numbers)
print("Unique سانلار:", unique_numbers)

# 3. Unique سانلارنىڭ سانى
print("Unique سانلارنىڭ سانى:", len(unique_numbers))