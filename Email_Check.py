class EmailCheck:
    def __init__(self, email):
        self.email = email

    def is_valid(self):
        if "@" in self.email and "." in self.email:
            return True
        else:
            return False
    
    def domain(self):
        f = 0
        i = 0
        while i < len(self.email):
            if self.email[i] == "@":
                f = 1
            if f > 0:
                print(self.email[i], end="")
            i += 1
        
text = input("Enter an email address: ")
obj = EmailCheck(text)

if obj.is_valid():
    print("Valid Email Address")
else:
    print("Invalid Email Address")

obj.domain()
