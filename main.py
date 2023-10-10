from hash_table import ChainingHashTable
from csv_data import load_package_data, get_package_data, Package, load_distance_array, load_address_array, \
    distance_between, address_index_lookup, Truck

my_hash = ChainingHashTable()
print('The empty hash table: ', my_hash.table, end='\n\n')
# print('')  # can be used to add a blank line at the end of the output instead of end='\n\n' in print() above.
load_package_data('packages.csv', my_hash)
# get_package_data(my_hash)  # uncomment this to print all the package data in the hash table.

# Proving an insert into the hash table works:
# package1 = Package(41, '321 Blastoff St', 'Beverly Hills', 'CA', 90210, '7:00 PM', 2, 'best driver ever!')
# my_hash.insert(41, package1)
# get_package_data(my_hash)  # to print again and show the added package in the hash table exists.

# loading arrays
distance_array = []
load_distance_array('distances.csv', distance_array)
address_array = []
load_address_array('addresses.csv', address_array)


print('Printing distance array data:')
for x in distance_array:
    print(x)
print('')

first_distance = distance_array[11][7]  # [0][0] = 0 output which is row 1 (because rows start counting at 1), index 0
# in distances.csv,
# [8][5] = 4.5 output which is row 9, index 5,
# [14][1] = 4.6 output which is row 15 index 1,
# [17][3] = 5.3 output which is row 18 index 3.
# [5][11] = blank output since row 6 index 11 has no data.
# [5][30] = IndexError since the index is out of the list's range.
second_distance = distance_array[3][25]  # should be blank or 10.1 miles

first_index = address_index_lookup('2835 Main St', address_array)  # row 12 AKA index 11
print(first_index)
second_index = address_index_lookup('2300 Parkway Blvd', address_array)  # row 8 AKA index 7
print(second_index)

print('Testing the distance array\'s output:\nThe distance from the address at index', first_index, ' to the address '
        'at index', second_index, ' is: ', first_distance, 'miles', end='\n\n')  # testing the distance array's
# output, hope its 4.8

third_index = address_index_lookup('1488 4800 S', address_array)  # index 3
print(third_index)
fourth_index = address_index_lookup('600 E 900 South', address_array)  # index 25
print(fourth_index)

print('Testing the distance array\'s output:\nThe distance from the address at index', third_index, 'to the address '
        'at index', fourth_index, ' is: ', second_distance, 'miles', end='\n\n')  # testing the distance array's
# output, should be either blank or 10.1

print('Using the distance_between function: ')
dist = distance_between('2835 Main St', '2300 Parkway Blvd', address_array, distance_array)
print('The distance between 2835 Main St and 2300 Parkway Blvd is: ', dist, 'miles')

dist = distance_between('1488 4800 S', '600 E 900 South', address_array, distance_array)
print('The distance between 1488 4800 S and 600 E 900 South is: ', dist, 'miles', end='\n\n')


print('The current address array looks like: \n', address_array, end='\n\n')

print('Printing address array data line by line:')
for x in address_array:
    print(x)
print('')

"""
for i in range(len(address_array)):
    print(address_array[i])
"""

"""
address_index_lookup('233 Canyon Rd', address_array)  # 233 Canyon Rd is located at index 8 since row1 is index 0 in
# addresses.csv, row2 is index 1, row 8 is index 7, etc.
print('')
address_index_lookup('', address_array)  # 233 Canyon Rd is located at index 8 since row1 is index 0 in
# addresses.csv, row2 is index 1, row 8 is index 7, etc.
print('')
dist = distance_between('233 Canyon Rd', '1330 2100 S', address_array, distance_array)
print('The distance between 233 Canyon Rd and 1330 2100 S is: ', dist, 'miles', end='\n\n')
"""

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
