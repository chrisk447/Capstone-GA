import flask
app = flask.Flask(__name__)

###### model goes here #######
import numpy as np 
import pandas as pd 
from time import strftime
import datetime
from os import listdir
import ast

# def clean_df(busy_dataframe):
#     '''Dropping columns that hold little to no information. Combining columns with relevant info.
#     Then reset the index since we are getting repeated indices'''
    
#     # Market DataFrame. If scraping, comes in ready form
#     # If pulling from old data, dictionary comes in string form
#     if isinstance(busy_dataframe.market.reset_index(drop=True)[0], str):
#         market_df = pd.DataFrame([ast.literal_eval(row) for row in busy_dataframe['market']])
#     else:
#         market_df = pd.DataFrame([row for row in busy_dataframe['market']])
        
#     # Same, but for including link for images
#     if isinstance(busy_dataframe.media.reset_index(drop=True)[0], str):
#         media_df = pd.DataFrame([ast.literal_eval(row) for row in busy_dataframe['media']])['thumbUrl']
#     else:
#         media_df = pd.DataFrame([row for row in busy_dataframe['media']])['imageUrl']
    
#     # Combine dataframes and drop unnecessary columns
#     cleaner_dataframe = busy_dataframe.join(market_df)
#     cleaner_dataframe = cleaner_dataframe.join(media_df)
    
#     cleanest_dataframe = cleaner_dataframe.drop(['breadcrumbs', 'childId', 'countryOfManufacture', 'type', 
#         'uuid', 'dataType', 'doppelgangers', 'condition', 'description', 'hidden', 'ipoDate', 'productCategory', 
#         'shoeSize', 'urlKey', 'charityCondition', 'releaseTime', 'shortDescription', 'media', '_highlightResult', 
#         'market', '_tags', 'id', 'objectID', 'lastHighestBidTime', 'lastLowestAskTime', 'styleId', 'productId',
#         'productUuid', 'skuUuid', 'updatedAt', 'traits', 'tickerSymbol', 'salesLastPeriod',
#         'minimumBid', 'averageDeadstockPriceRank', 'deadstockSoldRank', 'pricePremium', 'pricePremiumRank',
#         'salesThisPeriod', 'createdAt', 'lastSaleDate'], axis=1)
    
#     # Reset the index, since we are getting repeated indices
#     cleanest_dataframe.reset_index(drop=True, inplace=True)
    
#     return cleanest_dataframe

# def read_and_clean(path):
#     '''Read a file path where datasets are stored. Cleans the dataframe by removing duplicates,
#     removing first column (Unnamed: 0) to be ready for clean_df function.'''
#     file_list = listdir(path)
#     file_list.remove('dataio')
    
#     # Make a list of all the dataframes
#     parts_df = [pd.read_csv('../datasets/' + files) for files in file_list]
    
#     # Make one dataframe, take out first column and drop duplicates based on 'urlkey'
#     df = pd.concat(parts_df)
#     df = df.iloc[:,1:]
#     df.drop_duplicates(['uuid'], inplace=True)#, keep='last')
    
#     # Clean Brand names
#     df.brand = df.brand.map(lambda x: x.title())
    
#     # Lastly, change 'nan' to np.nan.
#     df = df.applymap(lambda x: np.nan if x=='nan' else x)

#     return df

# # Using functions defined above to read all previously downloaded data into one dataframe.
# path = '../datasets/'
# shoe = clean_df(read_and_clean(path))

# # Some cleaning first. Take out null rows and change time data to date time
# shoe.dropna(inplace=True)
# shoe['releaseDate'] = pd.to_datetime(shoe.releaseDate).dt.date
# shoe['year'] = pd.to_datetime(shoe.year.map(lambda x: str(int(x)))).dt.year

# # New metric for rarity of shoe & a boolean for those above median
# shoe['rarity'] = shoe.averageDeadstockPrice/shoe.retailPrice
# shoe['rarity_bool'] = shoe.rarity.map(lambda x: 1 if x >= shoe.rarity.median() else 0)

# # Since shoes retailed at $0 doesn't fit into the scope of the project, drop them.
# infinity_ind = shoe[shoe.retailPrice==0].index
# shoe.drop(infinity_ind, axis=0, inplace=True)
# shoe.reset_index(inplace=True, drop=True)

# # Concerned with only the top brands
# topshoes = shoe[(shoe.brand=='Adidas')|(shoe.brand=='Nike')|(shoe.brand=='Jordan')]
# topshoes.reset_index(drop=True, inplace=True)

# # Have to redefine the rarity cut-off
# topshoes['rarity_bool'] = topshoes.rarity.map(lambda x: 1 if x >= topshoes.rarity.median() else 0)



























# df = pd.read_csv('datasets/titanic.csv')
# include = ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Survived']

# # Create dummies and drop NaNs
# df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
# df = df[include].dropna()

# X = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp']]
# y = df['Survived']

# PREDICTOR = RandomForestClassifier(n_estimators=100).fit(X,y)


###### routes go here #######
@app.route('/predict', methods=["GET"])
def predict():
    pclass = flask.request.args['pclass']
    sex = flask.request.args['sex']
    age = flask.request.args['age']
    fare = flask.request.args['fare']
    sibsp = flask.request.args['sibsp']

    item = [pclass, sex, age, fare, sibsp]
    score = PREDICTOR.predict_proba(item)
    results = {'survival chances': score[0,1], 'death chances': score[0,0]}
    return flask.jsonify(results)

#--------------------Creating an API, method 2------------#

@app.route('/page')
def page():
   with open("page.html", 'r') as viz_file:
       return viz_file.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

       inputs = flask.request.form

       pclass = inputs['pclass'][0]
       sex = inputs['sex'][0]
       age = inputs['age'][0]
       fare = inputs['fare'][0]
       sibsp = inputs['sibsp'][0]

       item = np.array([pclass, sex, age, fare, sibsp])
       score = PREDICTOR.predict_proba(item)
       results = {'survival chances': score[0,1], 'death chances': score[0,0]}
       return flask.jsonify(results)

if __name__ == '__main__':

	HOST = '127.0.0.1'
	PORT = '4000'

	app.run(HOST,PORT)