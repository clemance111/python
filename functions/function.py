def first(first_name,last_name,age=18):
    if age<18:
        return "wrong age"
    return f"{first_name} {last_name} ,and age is: {age}"
print(first("cedro","eddy",15))