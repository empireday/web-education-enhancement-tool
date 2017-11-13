import requests #i dont use all request functions but im too lazy to change this for compression formatting.
import time
import getpass
#f*** smoothwall, as of writing this they implemented a feature that logged you outta the internet with a smoothwall webpage every 10 mins
#this program is for resending the TOTALLY UNENCRYPTED HTTP POST

#F*** SMOOTHWALL

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

-#YO I THOUGHT I NEEDED THIS SECTION WITH THE COOKIE BUT APPARENTLY THATS BULLS*** LOL,
-#kept for fun archive purposes.
-'''
-print ("Now pass the computer to the hackerman so he can sort out the cookie. ")
-time.sleep(5)
-print("Alternatively if you have a copy of securecookie already on your computer, please wait 5 seconds and input the value inside the text file.")
-time.sleep(5)
-var_cookie = input("ok dude last thing here is the only thing we need to get this going:     ")
-print("would you like to save this cookie? Y/N  ")
-save = input("Y/N   ")
-if save == ("Y", "y"):
-    f = open('securecookie.txt', 'w')
-    f.write(var_cookie)
-    '''
-
