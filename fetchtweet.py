    tweetlist = []
    entitylist = ['technology','mobile','tablets']
    listindex = 0
    import tweepy

    auth = tweepy.OAuthHandler("BB8uhuyrMzHesokpE7RqcYemc", "7YhL2UOSVoUyquuImiT1uOag0gS5HR3mrt7mmXrNZbwNHOVklF")
    auth.set_access_token("2330384770-kx4jr7mfUsCJod2MNuff3VzCh6tbGCvdymwp3ND",
                          "IMEYoDK2gZITSztqKQvHohTMOPkmEjsA0w6AOoECIdCqu")
    api = tweepy.API(auth)
    count = 0

    for i in range(20):
        for tweet in api.search(entitylist[listindex]):
            tweetlist.append(tweet.text)
        count += 1
        if count == 1000:
            listindex += 1
            count = 0

    print(tweetlist)
