import tweepy
import urllib2

#Python library that helps tranlate the Twitter API to the python program.  This
#library has a list of functions that will enable the program to communicate and
#work with Twitter.  We use urllib to open a poem generating website.

class TwitterAPI:
    def __init__(self):
        consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

#We make our own class, name it TwitterAPI, for a good deal of functions we are
#going to create.  We make a def __init__ so we can have the following variables
#initialized immediately when calling the class.  We make the argument (self)
#to reference the function itself within itself, creating an instance of 
#TwitterAPI, the place we reference it within itself is in self.API in the class.
#For creating an access token and keys, we research and follow these instructions
#(http://videlais.com/2015/03/02/how-to-create-a-basic-twitterbot-in-python/).


    def tweet(self, message):
        self.api.update_status(status=message)

#We make another function called tweet, which will update our message.  We make
#self the argument because we call the instance of self within TwitterAPI, as
#well as calling the instance of message.  We utiize the library of tweepy
#to update the status, and we equate whatever message we generate to be the
#status that is tweeted.

def getPoem():
    pageHTML = urllib2.urlopen("http://www.pangloss.com/seidel/Poem/poem.cgi").read()
    poem_text = ""
    line_list = pageHTML.splitlines()
   
#We create a function called "getPoem". The initial idea was to generate our own poems by importing
#a library dictionary, roll with a few adjectives, nouns, and verbs and connect them into generated
#sentences, but it proved tedious and painful - the results were also very nonsensical, and we
#decided to find a poem generator on the internet.  We found the url above, and instead, we rewrote
#the code.  We assigned pageHTML to the webpage, we used the urllib to open the page, and to read 
#the page.
    
    line4 = line_list[4]
    line4 = line4.replace("<p>","")
    poem_text = line4.strip() + "\n"

#We went to the webpage, viewed the source of the page, and notice that the poem that is
#generated lines 5-9.  Because in Python code lists are "0 based", we write the code to
#to start on 4.  We create the variable line4, and assign it from the line_list[4]. 
#Because that there are HTML code in the transferred data, we also make sure that line4
#have its <p> tag be replaced with an empty space, so it won't be printed.  We also
#assign that peom_text have line4 stripped of the extra new lines, so it can fit in a
#Twitter status.
    
    line6 = line_list[6]
    line6 = line6.replace("<br>","")
    poem_text = poem_text + line6.strip() + "\n"

#We do the same for line6 as we did for line4.  The source shows line 6 (which we would
#name line5) to be <br>, which is just a blank space in HTML.  This time, in the last
#line of code, we assign poem_text to have an addition to the new line, creating
#a bigger set of strings as we proceed through the code.
    
    line7 = line_list[7]
    line7 = line7.replace("<br>","")
    poem_text = poem_text + line7.strip() + "\n"

#Do the same for the 7th line.
    
    line8 = line_list[8]
    line8 = line8.replace("<br>","")
    poem_text = poem_text + line8.strip() + "\n"
    print poem_text
    return poem_text

#Do the same for the 8th line.

twitter = TwitterAPI()
poem =  getPoem()
twitter.tweet(poem)

#We assign the variable twitter to the TwitterAPI class we created, intiailizing no args.
#The class initializes the access tokens immediately so the program understands what
#account we are logging into.  We assign poem to the function getPoem, which will 
#generate a new poem each time this program is run.  Last but not least, we assign
#the twitter variable (that we created above) to tweet (by using the tweepy library)
#to print the arg poem.
