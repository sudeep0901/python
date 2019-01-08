
def retmul(text):
    # returning more than values from function using tuple
    return (text, 'one', 'two')

rt = retmul("Return more than  on value using tubple")

print(rt)

for val in rt:
    print(val)
    # val = "changed"

print(rt)