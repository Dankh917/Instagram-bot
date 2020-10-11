an instagram bot I created out of boredom using python and selenium.

what does the bot do:

1.login into your account 
2.follow your suggestions
3.unffollow people 
4.search for an hashtag you gave it and like al of the photos in that hashtag
*in case that instagram blocks you and asks for a code from gmail beacuse of suspicious behavior the bot knows how extract that code from gmail by itself and put it in the required place (this fuction takes some time as the program needs to wait for gmail to recive the e-mail from instagram)


how to use : 

first of all you'll have to enter the username and password of your instagram to the script (in file bot_functions line 17 for username and line 19 for password) 
then go to file main.py enter the hashtag you want to search for in line 11 (without the "#") and then simply run main.py
*in order for the program to pass the block if instagram blocks it and extract the code from gmail you will have to put the details of g-mail in gmail_code_extracter (line 6 for username and 7 for password )
            