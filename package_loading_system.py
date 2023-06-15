max_items = int(input("Enter the maximum number of items you would like to ship: "))

number_of_items = 0
package_weight = 0
package_counter = 1
total_weight_sent = 0
the_most_unused_package = 1
the_most_unused_space = 0

def check_total_unused_space(the_most_unused_package, the_most_unused_space, package_weight, package_counter):
    unused_space = 20 - package_weight
    if unused_space > the_most_unused_space:
        the_most_unused_space = unused_space
        the_most_unused_package = package_counter
    return the_most_unused_space, the_most_unused_package

while number_of_items != max_items:
    item_weight = int(input("What is your item's weight: "))
    if item_weight == 0:
        break
    if item_weight < 1 or item_weight > 10:
        print("Invalid weight!")
        continue
    number_of_items += 1
    if package_weight + item_weight > 20:
        total_weight_sent += package_weight
        the_most_unused_space, the_most_unused_package = check_total_unused_space(the_most_unused_package, the_most_unused_space, package_weight, package_counter)
        package_weight = item_weight
        print("Package " + str(package_counter) + " is full, sent without the new item.\n")
        package_counter += 1
        if number_of_items == max_items:
            total_weight_sent += package_weight
            the_most_unused_space, the_most_unused_package = check_total_unused_space(the_most_unused_package, the_most_unused_space, package_weight, package_counter)
            print("Package " + str(package_counter) + " is sent with the last item.\n")
            package_counter += 1
    elif package_weight + item_weight == 20:
        total_weight_sent += 20
        print("Package " + str(package_counter) + " is sent with the new item.\n")
        package_counter += 1
        package_weight = 0
    else:
        package_weight += item_weight
        print("The item is put inside the package.")
        if number_of_items == max_items:
            total_weight_sent += package_weight
            the_most_unused_space, the_most_unused_package = check_total_unused_space(the_most_unused_package, the_most_unused_space, package_weight, package_counter)
            print("Package " + str(package_counter) + " is sent with the last item.\n")
            package_counter += 1
            

print("Number of packages sent: " + str(package_counter - 1))
print("Total weight of the package sent: " + str(total_weight_sent) + "kg")
print("Total unused capacity: " + str(((package_counter-1)*20) - total_weight_sent) + "kg")
print("The most unused package: Package " + str(the_most_unused_package))
print("Unused weight in the most unused package: " + str(the_most_unused_space) + "kg")