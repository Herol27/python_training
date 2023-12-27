def int_to_roman(num: int):
    result = str()

    roman_nums = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    for roman in roman_nums:
        quotient = num // roman
        result += roman_nums[roman] * quotient
        num -= roman * quotient

    return result


if __name__ == '__main__':
    print(int_to_roman(33), "XXXIII")
    print(int_to_roman(54), "LIV")
    print(int_to_roman(1984), "MCMLXXXIV")
