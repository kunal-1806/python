def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for char in reversed(s):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    roman = []
    for i in range(len(val)):
        while num >= val[i]:
            num -= val[i]
            roman.append(syms[i])
    return "".join(roman)


# ---------------------------
# MAIN PROGRAM
# ---------------------------
user_input = input("Enter Roman numeral or Integer: ").strip()

if user_input.isdigit():  
    # Integer → Roman
    num = int(user_input)
    print("Roman:", int_to_roman(num))
else:
    # Roman → Integer
    roman = user_input.upper()
    print("Integer:", roman_to_int(roman))
