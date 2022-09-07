import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):

    if(re.fullmatch(regex, email)):
        print("Valid username")
 
    else:
        print("Invalid username")

if __name__ == '__main__':

    email = "rakesh326@gmail.com"

    check(email)
 
    email = "192012006.sse@saveetha.com"
    check(email)
 
    email = "arakesh326.com"
    check(email)

