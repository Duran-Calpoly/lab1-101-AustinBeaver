def calculate_average(num1,num2,num3):
    freedom = (num1+num2+num3)/3
    return freedom
print(calculate_average(6,7,8))

def add_tax(bill_total):
    new_bill = bill_total + 0.1*bill_total
    return new_bill
print(add_tax(8))

def greet_user(name):
    string1 = "Hello "
    string2 = name
    return string1 + string2
print(greet_user("William"))