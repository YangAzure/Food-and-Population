import unicodecsv as csv
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io

# Please go to Yelp API for a set of key
auth = Oauth1Authenticator(
consumer_key='',
consumer_secret='',
token='',
token_secret='')
client = Client(auth)
dicts_to_output = []

with open('Newyork.csv') as csvfile:
        nyc = csv.DictReader(csvfile)
        for k in nyc:
                params = {
                        'term' : 'food',
                        'location': k['JURISDICTION'],
                        'sort' : 1,
                        }
                res=client.search(**params).businesses
                for biz in res:
                        dicts_to_output.append({
                                'name': biz.name,
                                'id': biz.id,
                                'top_category': biz.categories[0].alias if biz.categories else '',
                                'rating': biz.rating,
                                'review_count': biz.review_count,
                                'postal_code': biz.location.postal_code
                        })
 
f = lambda x,y:x if y in x else x + [y]
dicts_to_output = reduce(f, [[], ] + dicts_to_output)                      
csv_keys = ['name', 'id', 'top_category', 'rating', 'review_count', 'postal_code']
with open('NYFoodYelp.csv', 'w') as output_file:
                        dict_writer = csv.DictWriter(output_file, csv_keys, quoting=csv.QUOTE_NONNUMERIC)
                        dict_writer.writeheader()
                        dict_writer.writerows(dicts_to_output)
                        
                        
                        
import numpy as np
data = np.genfromtxt('Newyork.csv', delimiter=',', skip_header=1,
                     skip_footer=10, names=['JURISDICTION', 'COUNT PARTICIPANTS', 'COUNT FEMALE', 'PERCENT FEMALE', 'COUNT MALE', 'PERCENT MALE', 'COUNT GENDER UNKNOWN', 'PERCENT GENDER UNKNOWN', 'COUNT GENDER TOTAL', 'PERCENT GENDER TOTAL', 'COUNT PACIFIC ISLANDER', 'PERCENT PACIFIC ISLANDER', 'COUNT HISPANIC LATINO', 'PERCENT HISPANIC LATINO', 'COUNT AMERICAN INDIAN', 'PERCENT AMERICAN INDIAN', 'COUNT ASIAN NON HISPANIC', 'PERCENT ASIAN NON HISPANIC', 'COUNT WHITE NON HISPANIC', 'PERCENT WHITE NON HISPANIC', 'COUNT BLACK NON HISPANIC', 'PERCENT BLACK NON HISPANIC', 'COUNT OTHER ETHNICITY', 'PERCENT OTHER ETHNICITY', 'COUNT ETHNICITY UNKNOWN', 'PERCENT ETHNICITY UNKNOWN', 'COUNT ETHNICITY TOTAL', 'PERCENT ETHNICITY TOTAL', 'COUNT PERMANENT RESIDENT ALIEN', 'PERCENT PERMANENT RESIDENT ALIEN', 'COUNT US CITIZEN', 'PERCENT US CITIZEN', 'COUNT OTHER CITIZEN STATUS', 'PERCENT OTHER CITIZEN STATUS', 'COUNT CITIZEN STATUS UNKNOWN', 'PERCENT CITIZEN STATUS UNKNOWN', 'COUNT CITIZEN STATUS TOTAL', 'PERCENT CITIZEN STATUS TOTAL', 'COUNT RECEIVES PUBLIC ASSISTANCE', 'PERCENT RECEIVES PUBLIC ASSISTANCE', 'COUNT NRECEIVES PUBLIC ASSISTANCE', 'PERCENT NRECEIVES PUBLIC ASSISTANCE', 'COUNT PUBLIC ASSISTANCE UNKNOWN', 'PERCENT PUBLIC ASSISTANCE UNKNOWN', 'COUNT PUBLIC ASSISTANCE TOTAL', 'PERCENT PUBLIC ASSISTANCE TOTAL'])
