import requests #i dont use all request functions but im too lazy to change this for compression formatting.
import time
import getpass
#f*** smoothwall, as of writing this they implemented a feature that logged you outta the internet with a smoothwall webpage every 10 mins
#this program is for resending the TOTALLY UNENCRYPTED HTTP POST



#this could be less ghetto but whatever lol
user = input("Put in your username my dude:   ")
print("thanks fam")

# I would prefer this line to show how many characters have been inputted, but it doesnt. if the password is wrong, you wont realise till you try to use the internet.
passvar = getpass.getpass('Now for the password- Ive set it so the characters are invisible so dont freak out:   ')


#this sends the post
loop = 1
while True:
    url = 'http://smoothwall.colchester.local'
    requests.post("http://smoothwall.colchester.local/iclogin", data={'USERNAME': user, 'PASSWORD': passvar, 'ACTION': "Login"})
    print("login request sent! Enjoy being logged in xd")
    time.sleep(90)
# 1:30 minute wait between requests please.
# Should be obvious as to why constant requests is bad
# OG post message was "F*** THE LEFT, TAXATION IS THEFT" because memes


