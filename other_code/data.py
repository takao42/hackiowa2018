from yelpapi import YelpAPI
yelp_api_key= "q80g0dgQbQvmO4xT0PBgtnOVr76Q0gUfhyhCj7o5E1TA_lNarvrSk-mAEVKV88cLmtM1k9kaJXcJO1LRNG-Vv3LG6F7Iu0EhpwUERd8p0O5aQAF2sQ_HDH5ip_e4W3Yx"
yelp_api = YelpAPI(yelp_api_key)





def getresturantresponse(area):
    return yelp_api.search_query(term='resturants', location=area, sort_by='rating', limit=50)


def getresturants(area):
    return getresturantresponse(area).get('businesses')


def getgetresturantsranking(area, index):
    resturants=getresturantresponse(area).get('businesses')
    return resturants[index]["rating"]


def getgetresturantslatidue(area, index):
    resturants=getresturantresponse(area).get('businesses')
    return resturants[index]["coordinates"]['latitude']


def getgetresturantslongtiude(area, index):
    resturants=getresturantresponse(area).get('businesses')
    return resturants[index]["coordinates"]['longitude']


def getreviewresponse(area, index):
    resturants = getresturantresponse(area).get('businesses')
    idforreview= resturants[index]['id']
    return yelp_api.reviews_query(id=idforreview)


def getreviewar(area, index):
    return getreviewresponse(area, index).get('reviews')

