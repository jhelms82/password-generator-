import random
import string

#Function for password, define character and password
def randomPassword(length):

       character = string.ascii_letters + string.digits + string.punctuation
       

       password =  ''.join(random.choice(character) for i in range(length))
       print("Your random password is: ", password)

randomPassword(8)