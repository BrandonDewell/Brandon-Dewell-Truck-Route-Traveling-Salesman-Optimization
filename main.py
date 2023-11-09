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

# this section proves the distance_between function is working.
"""
print('Using the distance_between function.  The first output is for a location on the bottom left of the '
      'addresses.csv file and the second is for the top right section that is blank in the same file, producing '
      'output proving that the function is working properly: ')
dist = csv_data.distance_between('2835 Main St', '2300 Parkway Blvd', address_array, distance_array)
print('The distance between 2835 Main St and 2300 Parkway Blvd is: ', dist, 'miles')

dist = csv_data.distance_between('1488 4800 S', '600 E 900 South', address_array, distance_array)
print('The distance between 1488 4800 S and 600 E 900 South is: ', dist, 'miles', end='\n\n')
"""

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

# t1_pkgs = [1, 29, 30, 31, 32, 34, 40, 2, 4, 5, 7, 10, 11, 12]  # leaves at 8am, 15 by 9am, must be delivered by
# 10:30am, 31 and 32 same address.
t1_pkgs = [1, 29, 30, 31, 34, 37, 40, 13, 14, 15, 16, 19, 20, 21, 38]
# t2_pkgs = [3, 18, 36, 38, 6, 37, 39, 8, 9]  # waits
# to leave until 9:05am, 6, 25 delivered by 10:30am, the rest must be delivered by the EOD, 8 and 9 same address,
# 25 and 26 same address, 37 and 38 same address, 3, 18, 36, 38 can only be on truck #2.

# t3_pkgs = [15, 13, 14, 16, 20, 21, 19, 28, 17, 22, 23, 24, 27, 33, 35, 25, 26]  # leaves at 8am, 13, 14, 16,
# 20 by 10:30am, 19 by EOD, and they all have to be delivered together, 15 and 16 same address, 20 and 21 same address.
t3_pkgs = [6, 25, 26]
t2_pkgs = [28, 32, 9, 5, 3, 18, 36, 38, 2, 4, 7, 8, 10, 11, 12, 17]

# package 9 wrong address is:  9,300 State St,Salt Lake City,UT,84103,EOD,2,Wrong address listed
# package 9 new address is:  9,410 S State St,Salt Lake City,UT,84111,EOD,2,Wrong address listed


# input('Enter the start of day time in hh:mm:ss :')
# TODO put in exceptions
start_time = '08:00:00'
h, m, s = start_time.split(':')
# time_object = datetime.timedelta(hours=8, minutes=0, seconds=0)
time_object_1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


# to print off the list of the packages in each list.
"""
print('t1 list: ', t1_pkgs)
print('t2 list: ', t2_pkgs)
print('t3 list: ', t3_pkgs, end='\n\n')
"""


truck1 = csv_data.Truck(1, t1_pkgs, time_object_1)
truck3 = csv_data.Truck(3, t3_pkgs, time_object_1)
truck2 = csv_data.Truck(2, t2_pkgs, time_object_1)

print('Truck 1 leaves at:', truck1.current_time)
print('This is truck1:', truck1, end='\n\n')


time_object_3 = datetime.timedelta(hours=int(1), minutes=int(5), seconds=int(1))  # adjust truck3 start time
truck3.current_time = truck3.current_time + time_object_3
truck3.time_left_hub = truck3.current_time
print('Truck 3 leaves at:', truck3.current_time)
print('This is truck3:', truck3, end='\n\n')

# time_object = datetime.timedelta(hours=int(1), minutes=int(5), seconds=int(1))

time_object_2 = datetime.timedelta(hours=int(2), minutes=int(20), seconds=int(1))
truck2.current_time = truck2.current_time + time_object_2  # use this to change the start time when a truck leaves.
truck2.time_left_hub = truck2.current_time
print('Truck 2 leaves at:', truck2.current_time)
print('This is truck2 with updated current time and start time:', truck2, end='\n\n')


print('truck 1 has these', len(truck1.packages), 'packages: ', truck1.packages)  # truck1 is the truck object,
# .packages is a field in the Truck class which holds the list.
print('truck 2 has these', len(truck2.packages), 'packages: ', truck2.packages)
print('truck 3 has these', len(truck3.packages), 'packages: ', truck3.packages, end='\n\n')

# csv_data.min_distance_from('4001 South 700 East', truck1.packages)
"""
next_truck_pkg = csv_data.min_distance_from(address_array[0], truck1, address_array, distance_array, my_hash)
print('')
print(next_truck_pkg)
print(next_truck_pkg[2])
total_miles = next_truck_pkg[2]
print(total_miles)
"""
# print(csv_data.min_distance_from('4001 South 700 East', truck2, address_array, distance_array, my_hash), end='\n\n')
# print(csv_data.min_distance_from('4001 South 700 East', truck3, address_array, distance_array, my_hash), end='\n\n')

truck1_dist, go_to_hub_dist_t1 = csv_data.deliver_pkgs(truck1, address_array, distance_array, my_hash)
print('')
truck3_dist, go_to_hub_dist_t3 = csv_data.deliver_pkgs(truck3, address_array, distance_array, my_hash)
print('')
truck2_dist, go_to_hub_dist_t2 = csv_data.deliver_pkgs(truck2, address_array, distance_array, my_hash)
print('')


print('Truck #1\'s total distance is: ', truck1_dist, 'miles, of which returning to the hub is: ', go_to_hub_dist_t1, 'miles.')
print('Truck #2\'s total distance is: ', truck2_dist, 'miles, of which returning to the hub is: ', go_to_hub_dist_t2, 'miles.')
print('Truck #3\'s total distance is: ', truck3_dist, 'miles, of which returning to the hub is: ', go_to_hub_dist_t3, 'miles.')
print('The total distance travelled by all three trucks is', truck1_dist + truck2_dist + truck3_dist, 'miles.')
print('')

print('pkg#, del address, del city, del state, del zipcode, weight, special notes, location, truck # package is on, '
      'time left hub, delivery dead line, time delivered')
for i in range(1, 41):
    print(my_hash.lookup(i))

# t1_pkgs = [1, 29, 30, 31, 34, 37, 40, 13, 14, 15, 16, 19, 20, 21, 38]
