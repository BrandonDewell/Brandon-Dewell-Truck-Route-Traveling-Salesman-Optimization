import datetime
import hash_table
import csv_data

my_hash = hash_table.ChainingHashTable()
# print('The empty hash table: ', my_hash.table, end='\n\n')
# print('')  # can be used to add a blank line at the end of the output instead of end='\n\n' in print() above.
csv_data.load_package_data('packages.csv', my_hash)
# get_package_data(my_hash)  # uncomment this to print all the package data in the hash table.


# this section proves an insert into the hash table works:
"""
package1 = Package(41, '321 Blastoff St', 'Beverly Hills', 'CA', 90210, '7:00 PM', 2, 'best driver ever!')
my_hash.insert(41, package1)
get_package_data(my_hash)  # to print again and show the added package in the hash table exists.
"""

# loading arrays
distance_array = []
csv_data.load_distance_array('distances.csv', distance_array)
address_array = []
csv_data.load_address_array('addresses.csv', address_array)

# this section outputs the distance array to prove it is working
"""
print('Printing distance array data:')
for x in distance_array:
    print(x)
print('')
"""

# this section outputs a test of the address_index_lookup
"""
first_distance = distance_array[11][7]  # [0][0] = 0 output which is row 1 (because rows start counting at 1), index 0
# in distances.csv,
# [8][5] = 4.5 output which is row 9, index 5,
# [14][1] = 4.6 output which is row 15 index 1,
# [17][3] = 5.3 output which is row 18 index 3.
# [5][11] = blank output since row 6 index 11 has no data.
# [5][30] = IndexError since the index is out of the list's range.
second_distance = distance_array[3][25]  # should be blank or 10.1 miles

first_index = csv_data.address_index_lookup('2835 Main St', address_array)  # row 12 AKA index 11
# print(first_index)
second_index = csv_data.address_index_lookup('2300 Parkway Blvd', address_array)  # row 8 AKA index 7
# print(second_index)

print('Testing the distance array\'s output:\nThe distance from the address at index', first_index, 'to the address '
        'at index', second_index, 'is: ', first_distance, 'miles', end='\n\n')  # testing the distance array's output.

third_index = csv_data.address_index_lookup('1488 4800 S', address_array)  # index 3
# print(third_index)
fourth_index = csv_data.address_index_lookup('600 E 900 South', address_array)  # index 25
# print(fourth_index)

print('Testing the distance array\'s output:\nThe distance from the address at index', third_index, 'to the address '
        'at index', fourth_index, ' is: ', second_distance, 'miles', end='\n\n')  # testing the distance array's
# output, should be either blank or 10.1
"""

print('Using the distance_between function.  The first output is for a location on the bottom left of the '
      'addresses.csv file and the second is for the top right section that is blank in the same file, producing '
      'output proving that the function is working properly: ')
dist = csv_data.distance_between('2835 Main St', '2300 Parkway Blvd', address_array, distance_array)
print('The distance between 2835 Main St and 2300 Parkway Blvd is: ', dist, 'miles')

dist = csv_data.distance_between('1488 4800 S', '600 E 900 South', address_array, distance_array)
print('The distance between 1488 4800 S and 600 E 900 South is: ', dist, 'miles', end='\n\n')

# this section prints the address array
"""
print('The current address array looks like: \n', address_array, end='\n\n')

print('Printing address array data line by line:')
for x in address_array:
    print(x)
print('')


# a different way to print the address array
for i in range(len(address_array)):
    print(address_array[i])
"""

# this section tests the address index lookup
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

# other stuff for asking for an input within the console and showing how %s and its replacement works in a string.
"""
name = input("who are you? ")
print("hello %s" % (name,))
"""

"""
t1 = [csv_data.get_package_info(my_hash, 1), csv_data.get_package_info(my_hash, 29),
      csv_data.get_package_info(my_hash, 30), csv_data.get_package_info(my_hash, 31),
      csv_data.get_package_info(my_hash, 34), csv_data.get_package_info(my_hash, 37),
      csv_data.get_package_info(my_hash, 40)]  
"""

t1 = [1, 29, 30, 31, 34, 37, 40]  # leaves at 8am, must be delivered by 10:30am.
t2 = [6, 25, 28, 32, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 21, 22, 23, 24, 26, 27, 33, 35, 36, 38,
      39]  # waits to leave until 9:06am, 6, 25 delivered by 10:30am, the rest must be delivered by the EOD.
t3 = [15, 13, 14, 16, 20,
      19]  # leaves at 8am, 15 by 9am, 13, 14, 16, 20 by 10:30am, 19 by EOD, and they all have to be delivered together.

# input('Enter the start of day time in hh:mm:ss :')
# TODO put in exceptions
start_time = '8:00:00'
h, m, s = start_time.split(':')
# time_object = datetime.timedelta(hours=8, minutes=0, seconds=0)
time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

print('t1 list: ', t1, '\n', 't2 list: ', t2, '\n', 't3 list: ', t3, '\n')


truck1 = csv_data.Truck(t1, time_object)
print(truck1.current_time)
truck2 = csv_data.Truck(t2, time_object)
print('This is truck2', truck2)
truck3 = csv_data.Truck(t3, time_object)
print(truck3.current_time)

time_object = datetime.timedelta(seconds=127)
truck1.current_time = truck1.current_time + time_object
print(truck1.current_time)
print('truck 1 has these packages: ', truck1.packages)  # truck1 is the truck object, .packages is a field in the
# Truck class which holds the list.
print('truck 2 has these packages: ', truck2.packages)
print('truck 3 has these packages: ', truck3.packages)

# csv_data.min_distance_from('4001 South 700 East', truck1.packages)
csv_data.min_distance_from('4001 South 700 East', truck1)
