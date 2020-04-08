from InstagramAPI import InstagramAPI
from time import sleep
import datetime
import urllib.request
import pprint
import httplib2
import requests
def get_media_id(url):
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    media_id = req.json()['media_id']
    return media_id


api = InstagramAPI('USER  ID, PASS,)



api.getSelfUserFeed()
# api.like('66295846_124477332116234_8622439205231978201_n')
# api.follow('14486256592')
# listt = api.getMediaComments("1982048137293633916_2040806056")
# print(listt)

api.getSelfUserFeed()
result = api.LastJson
print(result)
while(1):
    api.getMediaLikers('1982048137293633916_2040806056')
    # api.comment('2080506456458503784_2040806056',"new comment") first parameter is media_key and second is new comment for a post
    result = api.LastJson
    # num_comments= result['media']['comment_count']


    print("LIKES ="+str(len(result["users"])))

    api.editMedia('1982048137293633916_2040806056',"This post has " +str(len(result['users']))+" likes recent update on "+str(datetime.datetime.now()) +" PST")
    print(datetime.datetime.now())
    sleep(20)
