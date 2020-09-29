list1 = [1, 2, 3, 5, 5, 7, 8]

def remove_duplicates(list1):
    list2 = []
    if list1:
        for item in list1:
            if item not in list2:
                list2.append(item)

    else:
        return list1

    return list2

print(remove_duplicates(list1))

#################################

Celsius = int(input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")

############################