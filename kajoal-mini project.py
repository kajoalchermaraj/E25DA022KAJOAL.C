import re
def password _strength(password):
    length_ok =len(password)>=8
    upper_ok= any(ch.isupper() for ch in password)
    lower_ok=any(ch.islower()for ch in password)
    digit _ok=any(ch.isdigit() for ch in password)
    special_ok=re.search(r"[!@#$%^&*()\-_=+[\];:'\",.<>?/'~]",password)is not none
    score=sum([length_ok,upper_ok,lower_ok,digit_ok,special_ok])
    if score==5
    print("strong password")
elif 3<=score<5:
    print("Medium password")
else:
    print("Weak password")
    user_password=input("Enter your password")
    password_stength(use_password)
