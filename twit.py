import tweepy
class Twit:
    def search(self, username):
        auth = tweepy.OAuthHandler("[YOUR OUTH HANDLER KEY]",
                                       "[YOUR AUTH HANDLER KEY 2]")
        auth.set_access_token("[YOUR ACCESS TOKEN]",
                                  "[YOUR ACCESS TOKEN 2]")

        api = tweepy.API(auth)

        user = api.get_user(username)
        return user

    def tweets(self, username):
        auth = tweepy.OAuthHandler("[YOUR OUTH HANDLER KEY]",
                                       "[YOUR AUTH HANDLER KEY 2]")
        auth.set_access_token("[YOUR ACCESS TOKEN]",
                                  "[YOUR ACCESS TOKEN 2]")

        api = tweepy.API(auth)

        tweets = api.user_timeline(screen_name = username, count = 50)
        return tweets
