import streamlit as st

def roman_to_int(roman_str):
    dict_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0

    roman_str = roman_str.replace("IV", "IIII")
    roman_str = roman_str.replace("IX", "VIIII")
    roman_str = roman_str.replace("XL", "XXXX")
    roman_str = roman_str.replace("XC", "LXXXX")
    roman_str = roman_str.replace("CD", "CCCC")
    roman_str = roman_str.replace("CM", "DCCCC")
    my_str = list(roman_str)
    for char in my_str:
        num = num + dict_roman[char]
    return num

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def main():
    st.title("Converter")

    option = st.selectbox("Select Conversion", ("Roman to Integer", "Integer to Roman"))

    if option == "Roman to Integer":
        roman_input = st.text_input("Enter Roman Numeral")
        if st.button("Convert"):
            if roman_input:
                try:
                    integer_output = roman_to_int(roman_input)
                    st.success(f"The integer equivalent is: {integer_output}")
                except ValueError:
                    st.error("Invalid Roman numeral")
            else:
                st.warning("Please enter a Roman numeral")

    elif option == "Integer to Roman":
        integer_input = st.number_input("Enter Integer")
        if st.button("Convert"):
            if integer_input:
                integer_input = int(integer_input)
                if integer_input <= 0:
                    st.error("Please enter a positive integer")
                else:
                    roman_output = int_to_roman(integer_input)
                    st.success(f"The Roman numeral equivalent is: {roman_output}")
            else:
                st.warning("Please enter an integer")

if __name__ == "__main__":
    main()
