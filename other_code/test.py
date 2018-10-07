from yelpapi import YelpAPI
import argparse
from pprint import pprint
key= "q80g0dgQbQvmO4xT0PBgtnOVr76Q0gUfhyhCj7o5E1TA_lNarvrSk-mAEVKV88cLmtM1k9kaJXcJO1LRNG-Vv3LG6F7Iu0EhpwUERd8p0O5aQAF2sQ_HDH5ip_e4W3Yx"
yelp_api = YelpAPI(key)

#bussiness array
response = yelp_api.search_query(term='burrito', location='ames', sort_by='rating', limit=9)

businesses = response.get('businesses')
#bussiness array

#bussiness id
business_id = businesses[0]["coordinates"]['longitude'] #just change to get name or ranking or location
#bussniess id

#reviews array
#response2 = yelp_api.reviews_query(id=business_id)

#reviews = response2.get('reviews')
#reviewss array

#print(response)
print(business_id)
#print(reviews[2]['text'])