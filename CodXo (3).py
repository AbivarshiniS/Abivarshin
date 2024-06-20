import randam
import string
length=int(input("Enter Length Number:"))
chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation
password="".join([random.choice(chars)for i in range(length)])
print("Your Password is:",password)           
           
