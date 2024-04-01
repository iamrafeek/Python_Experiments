import streamlit as st
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now().date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        months = 12 - birth_date.month + today.month - 1
    else:
        months = today.month - birth_date.month
    if today.day < birth_date.day:
        days = birth_date.day - today.day
    else:
        days = today.day - birth_date.day
    return age, months, days

def main():
    st.title("Age Calculator")
    
    birth_date = st.date_input("Enter your date of birth")
    
    if st.button("Calculate Age"):
        age, months, days = calculate_age(birth_date)
        st.write(f"You are {age} years, {months} months, and {days} days old.")

if __name__ == "__main__":
    main()
