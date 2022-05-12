def isnumber(value):
    try:
        float(value)
        return True
    except:
        return False


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

    return "There is no such Key"


def first_letter_upper(string):
    array = list(string)
    return f'{array[0].upper()}{"".join(array[1:]).lower()}'


def duas_casas(num):
    if num // 1 == num / 1:
        return f'{num}.00'
    return num
