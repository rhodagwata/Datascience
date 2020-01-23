# Realestatepredictor project Overview
Realestatepredictor is a predicting system meant to solve a business problem.
The data used is acquired from a large Real Estate Investment Trust(REIT) company,this company invests in houses and aparments within a small county in New York Estate and they require to predict fair transaction price of a property before it is sold.

#problem statement
The dataset used in this project has been obtained from transaction prices for previous properties on the
market.It was collected in 2016 and one is expected to build a real-estate pricing model using that dataset.
The model is expected to predict transaction prices with an average error of under US
Dollars 70,000, for the clients to be very satisfied with this resultant model.

#Business Objectives and Constraints
Deliverable: Trained model file
Win condition: Avg. prediction error < $70,000
Model Interpretability will be useful
No latency requirement

#Data Overview
The dataset has 1883 observations in the county where the REIT operates.
 Each observation is for the transaction of one property only.
 Each transaction was between $200,000 and $800,000.
 
 #Target variable
 'tx_price' is theTransaction price in USD
 
 #Features of the data:
Public records:
'tx_year' - Year the transaction took place 'property_tax' - Monthly property tax
'insurance' - Cost of monthly homeowner's insurance

#Property characteristics:
'beds' - Number of bedrooms
'baths' - Number of bathrooms
'sqft' - Total floor area in squared feet
'lot_size' - Total outside area in squared feet
'year_built' - Year property was built
'active_life' - Number of gyms, yoga studios, and sports venues within 1 mile
'basement' - Does the property have a basement?
'exterior_walls' - The material used for constructing walls of the house
'roof' - The material used for constructing the roof

#Location convenience scores:
'restaurants' - Number of restaurants within 1 mile
'groceries' - Number of grocery stores within 1 mile
'nightlife' - Number of nightlife venues within 1 mile
'cafes' - Number of cafes within 1 mile
'shopping' - Number of stores within 1 mile
'arts_entertainment' - Number of arts and entertainment venues within 1 mile
'beauty_spas' - Number of beauty and spa locations within 1 mile
'active_life' - Number of gyms, yoga studios, and sports venues within 1 mile

#Neighborhood demographics:
'median_age' - Median age of the neighborhood
'married' - Percent of neighborhood who are married
'college_grad' - Percent of neighborhood who graduated college

#Schools:
'num_schools' - Number of public schools within district
'median_school' - Median score of the public schools within district, on the range 1 - 10

#Mapping business problem to ML problem
I have used liner regression to predict the transaction price of the house given the features I have mentioned above.



