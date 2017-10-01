#from twitter import Twitter
import time
import tweepy
from tweepy.auth import OAuthHandler
import json
ACCESS_TOKEN = '902949052681203729-mnu26NivP5AOWU0Z699AVi961uEmDnK'
ACCESS_SECRET = 'cY7RDS5N4ji1MK4UGzd9KDcnojNtcFJpNPSMfk4qTvp6Y'
CONSUMER_KEY = 'ygZoXjDPDsEDjJZwNeBCeRjQU'
CONSUMER_SECRET = 'Ho8BGVgES3Ua4eCLOQa5sqei5LXPmNizGvliz34MChdAuLOJh0'
#oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
print"Hello Welcome to the twitter panel"
time.sleep(4)
print "Choose the options you need to do.."
print "1)Tweet something\n2)Get your follower list\n3)get the latest tweets\n4)Search a tweet based on the query\n5)Delete a tweet based on the query\n6)Tweet something using media\n7)Follow a friend\n8)Unfollow a friend\n9)Check the friendship between the users\n10)Block a user\n11)unblock a user\n12)Create a list"
user_choice=input("Enter your choice")
if(user_choice==1):
    print "You need to sweet something.."
    message=raw_input("Enter the status you need to update")
    api.update_status(message)
elif(user_choice==2):
    print "You need to get your follower list"
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print followers.screen_name
elif(user_choice==3):
    print "You want to get the latest tweet"
    public_tweets=api.home_timeline()
    for tweet in public_tweets:
        print tweet.text
elif(user_choice==4):
    print "You need to search the trending tweet based on a query"
    query=raw_input("Enter the query which will be the basis to search the tweet")
    for tweet in tweepy.Cursor(api.search,q=query).items():
        try:
            print ('tweet by @ '+tweet.user.screen_name)
        except tweept.Tweeperror as e:
            print e.reason
        retweet=raw_input("Do you want to tweet this tweet again?")
        if(retweet.upper()=='YES'):
            tweet.retweet()
            print "Retweeted"
        else:
                print "Ok"
        favourite=raw_input('Do you want to favourite this tweet?')
        if(favourite.upper()=='YES'):
            tweet.favourite()
            print "Favourited.."
        else:
            print "Ok"
elif(user_choice==5):
    print "Delete a tweet"
    tids=[]
    for status in tweepy.Cursor(api.user_timeline).items():
        tids.extend(status.id)
        print '{'
        print status.id
        print status.text
        print '}'

    print "Copy paste the id corresponding to the status you need to delete"
    delete_id=raw_input('-->')
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(delete_id)
        except tweepy.Tweeperror as e:
            print e.reason
elif(user_choice==6):
    print "You need to update a status with media"
    media_url=raw_input('enter the media url of the photo/video/other you need to upload')
    status=raw_input('Enter the status you need to upload')
    api.update_with_media(status,media)
elif(user_choice==7):
    print "okay so you need to make friends.. :)"
    friend=raw_input("Enter the correct username")
    try:
        api.create_friendship(friend)
        print "Followed"
    except tweepy.Tweeperror as e:
        print e.reason
elif(user_choice==8):
    print "Ohh..is there any enimity cooking.. ROFL..loll"
    enemy("Enter the username of the one you need to unfollow")
    try:
        api.destroy_friendship(enemy)
        print "Unfollowed.."
    except tweepy.Tweeperror as e:
        print e.reason
elif(user_choice==9):
    print "So you need to check the friendship between two individuals"
    user_1=raw_input("enter the username of the user-1")
    user_2=raw_input("enter the username of the user-2")
    try:
        api.exists_friendship(user_1,user_2)
    except tweepy.Tweeperror as e:
        print e.reason
elif(user_choice==10):
    print "Do you really want to block the user"
    reply=raw_input('==>')
    if(reply.upper=='YES'):
        user=api.get_user(raw_input("enter the username"))
        x=user.id
        api.create_block(x)
    else:
        print "Huhh..chillax dude"
elif(user_choice==11):
    print "uhh..u need to unblock the user.."
    y=raw_input("enter the username")
    api.destroy_block(y)
elif(choice==12):
    print "you ned to create the list"
    name=raw_input("enter the name of the list")
    mode=raw_input("public or private")
    description=raw_input("give some description")
    api.create_list(name,mode,description)

else:
    print "Okay so you need to create 
    print "Bye bye"
    
    '''
tweet="#3"
twe=api.update_status(tweet)
getid=twe.id
print getid
'''
