from hash_table import ChainingHashTable
from csv_data import load_package_data, get_package_data, Package, load_distance_array, load_address_array

my_hash = ChainingHashTable()
print('The empty hash table: ', my_hash.table, end='\n\n')
# print('')  # can be used to add a blank line at the end of the output instead of end='\n\n' in print() above.
load_package_data('packages.csv', my_hash)
get_package_data(my_hash)


# Proving an insert into the hash table works:
# package1 = Package(41, '321 Blastoff St', 'Beverly Hills', 'CA', 90210, '7:00 PM', 2, 'best driver ever!')
# my_hash.insert(41, package1)
# get_package_data(my_hash)  # to print again and show the added package in the hash table exists.


distance_array = []
load_distance_array('distances.csv', distance_array)
first_distance = distance_array[12][7]  # [0][0] = 0 output which is row 1, index 0 in distances.csv,
# [8][5] = 4.5 output which is row 9, index 5,
# [14][1] = 4.6 output which is row 15 index 1,
# [17][3] = 5.3 output which is row 18 index 3.
# [5][11] = blank output since row 6 index 11 has no data.
# [5][30] = IndexError since the index is out of the list's range.
print('Testing the distance array\'s output: ' + first_distance, end='\n\n')  # testing the distance array's output


print('Printing distance array data:')
for x in distance_array:
    print(x)
print('')

address_array = []
load_address_array('addresses.csv', address_array)
first_index = address_array.index('233 Canyon Rd')  # which is located at index 8 since row1 is index 0 in
# addresses.csv, row2 is index 1, row 8 is index 7, etc.
print('The address index you entered is: ', first_index, end='\n\n')
print('The address array is: \n', address_array, end='\n\n')

"""
for i in range(len(address_array)):
    print(address_array[i])
"""

print('Printing address array data line by line:')
for x in address_array:
    print(x)
