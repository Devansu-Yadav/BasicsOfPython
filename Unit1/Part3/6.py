def scope_variable():
    print(msg)
    # This code shows error because we are referencing 'msg' before assignment inside the function.
    # If we comment the line below no error will be shown.
    msg = "This is local variable" 
    print(msg)

msg = "This is Global variable"
scope_variable()
print(msg)


# Corrected Code:-
# Uncomment this code to use this code and comment the above code.
# def scope_variable():
#     # If we comment the line below no error will be shown.
#     global msg
#     print(msg)
#     msg = "This is local variable" 
#     print(msg)

# msg = "This is Global variable"
# scope_variable()
# print(msg)