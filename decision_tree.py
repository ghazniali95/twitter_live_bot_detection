from __future__ import division
import twit
import datetime
import re
class DTree:
    returndata = {}
    username = None
    def test(self, username):
        self.username = username
        t = twit.Twit()
        user = t.search(username)

        #RULE status view
        self.returndata["status_count"] = str(user.statuses_count)
        self.returndata["days"] = str((datetime.datetime.now().date() - user.created_at.date()).days)
        self.returndata["status_entropy"] = user.statuses_count/(datetime.datetime.now().date() - user.created_at.date()).days

        #RULE banner if null
        if hasattr(user, 'profile_banner_url'):
            self.returndata["banner"] = user.profile_banner_url
        else:
            self.returndata["banner"] = "empty"

        #RULE geo enabled not true in bots
        self.returndata["geo_enabled"] = user.geo_enabled

        # RULE favourite count / status count if high then bot
        self.returndata["favCount"] = user.favourites_count
        self.returndata["favCount_entropy"] = user.statuses_count / (user.favourites_count if user.favourites_count > 0 else 1)

        #RULE if verified
        self.returndata["verified"] = user.verified
        self.postCheck()

        # print self.returndata
        return self.result()

    def postCheck(self):
        t = twit.Twit()
        user = t.tweets(self.username)

        urls = []
        count = 0
        for i in user:
            # print i.text
            if len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', i.text)) > 0:
                urls.append(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', i.text))
            # get tags from posts
            # print set([i[1:] for i in i.text.split() if i.startswith("#")])
            count += 1
        self.returndata["links"] = len(urls)/count if count > 0 else 1
        return


    def result(self):
        geoEnabled = 80
        profileBanner = 70
        statusCount = 40
        favCount = 75
        links = -20
        result = 0
        if not self.returndata["geo_enabled"]:
            result += geoEnabled
        if self.returndata["banner"] == "empty":
            result += profileBanner
        if self.returndata["status_entropy"] < 200:
            result += statusCount
        if self.returndata["favCount_entropy"] > 10:
            result += favCount
        if self.returndata["links"] < 0.3:
            result += links
        if self.returndata["verified"]:
            result = 0

        # print result
        if result > 120:
            return "Its a bot | Status: " + str(self.returndata["status_entropy"]) + " | Favourite: " + str(self.returndata["favCount_entropy"]) + " | Probability: " + str(1/result)
        else:
            return "This is a Human | Status: " + str(self.returndata["status_entropy"]) + " | Favourite: " + str(self.returndata["favCount_entropy"]) + " | Probability: " + str(1/result)
