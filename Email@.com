14. take an email address and check whether it contains @ and .com

email=input("Enter email:")
email1 = email.find("@")!=- email.find(".com")!=-1
print(email1)
