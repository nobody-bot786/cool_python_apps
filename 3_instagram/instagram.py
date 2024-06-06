from instabot import Bot
bot = Bot()
bot.login(username="nobody_bot786", password="mohdabid")

######  upload a picture #######
bot.upload_photo("", caption="")

######  follow someone #######
bot.follow("mr_nobody.786")

######  send a message #######
bot.send_message("hlo🤗 mention aa gye har jgha se 🤧ignor ko kar sharm to ayi nhi hogi🤣🤣jo yaha bhi muh uhta ke chale👀 aye😁🤣 tumhari ko self respect nhi kya🙄🌚", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("anyone")
for follower in my_followers:
    print(follower)

bot.(activ)
