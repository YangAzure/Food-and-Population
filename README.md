# Food-and-Population

This is a project about studying the relationship between population composition and food preference. You can get the data resource and plots in this proposal.

Dataset used:

1. Newyork.csv

Retrieved from NYC Open Data (https://data.cityofnewyork.us/City-Government/Demographic-Statistics-By-Zip-Code/kku6-nxdu)

This dataset is demographic statistics broken down by postal code in New York City. It demonstrates the population composition of each part, devided by postal code. Demographic statistics shows the distribution of population, which in this file, distributions of gender, race, and financial assistance condition is offered. 

2. NYFoodYelp.csv

Retrieved from Yelp API (https://www.yelp.com/developers). Code for retrieving can be found in yelpdata.py. 

For each API call, we can get the restaurants closest to the postal code we are searching. I searched all postal codes provided in Newyork.csv, and deleted the duplicated responses, stored the data in NYFoodYelp.csv. In this data file, 5 attributes are stored. The name of business, the yelp ID for them, their first categories which shows best of their food genre, ratings, review counts, and their postal codes. From ratings and review counts, we can know the popularity of the restaruants. And I also did some more pre-processing like deleting the empty rows. You can also find this part of code in yelpdata.py.

Plots provided:

1. fdFrequencybyPostal.png

This figure shows the density of restaurants by postal codes. Generated from NYFoodYelp.csv, and limited the area to the areas listed in Newyork.csv since when performing a serach there will be a radius from Yelp, and it will go beyond the areas used in this study a bit.

2. ppFrequencybyPostal.png

This figure shows the population density by postal codes. Generated from Newyork.csv. 
