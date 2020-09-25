def helloworld(yourname,greet="Hello "):
    return greet+yourname


a = helloworld(yourname="Devansu")
print(a)


# def greet(first_name, last_name):
#     print(first_name + " " + last_name)
#     return

# greet(first_name="John", "Smith")
# throws an error, positional argument follows keyword argument meaning first a positional argument must be passed and
# then a keyword argument