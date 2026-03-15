import re

text = "My phone number is 9876543210 and email is test@example.com"

# Match phone number
phone = re.findall(r"\d{10}", text)  
print("Phone:", phone)

# Match email
email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-z]{2,}", text)  
print("Email:", email)
