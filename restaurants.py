from yelpapi import YelpAPI
from utilities import print_dict

yelp_api_key = "q80g0dgQbQvmO4xT0PBgtnOVr76Q0gUfhyhCj7o5E1TA_lNarvrSk-mAEVKV88cLmtM1k9kaJXcJO1LRNG-Vv3LG6F7Iu0EhpwUERd8p0O5aQAF2sQ_HDH5ip_e4W3Yx"
yelp_api = YelpAPI(yelp_api_key)


def get_restaurants_by_location(location):
    return yelp_api.search_query(term='resturants',
                                 location=location,
                                 sort_by='rating',
                                 limit=50)


def get_restaurants_by_coordinate(latitude, longitude):
    return yelp_api.search_query(term='resturants',
                                 latitude=latitude,
                                 longitude=longitude,
                                 sort_by='rating',
                                 limit=50)


def get_review_by_id(id):
    return yelp_api.reviews_query(id=id)


if __name__ == '__main__':
    print_dict(get_restaurants_by_location('ames, iowa'))
    # print_dict(get_review_by_id("MsMA6RCi6kYutHFg8VQe-g"))

