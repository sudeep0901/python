string = "I am sudeep patel   "

split = string.split(',')
print(split)


string = "I am sudeep patel   "

split = string.split(' ', maxsplit=-11)  # -ve max split does not impact string
print(split)


input_string = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""


# cleaning up CSV data
def string_split(unsplit):

    results = []

    for line in unsplit.split('\n')[1:]:
        results.append(line.split(',', maxsplit=2))

    return results


print(string_split(input_string))

# Concatenating and Joining Strings

strings = ['do', 're', 'mi']

print("Hello".join(strings))

input_list = [
    ['Boston', 'MA', '76F', '65% Precip', '0.15 in'],
    ['San Francisco', 'CA', '62F', '20% Precip', '0.00 in'],
    ['Washington', 'DC', '82F', '80% Precip', '0.19 in'],
    ['Miami', 'FL', '79F', '50% Precip', '0.70 in']
]

joined = [','.join(row) for row in input_list]
print(joined)

for j in joined:
    print(j)
