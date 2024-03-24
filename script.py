import pandas as pd
#import codecademylib3
from surprise import Reader

book_ratings = pd.read_csv('goodreads_ratings.csv')
print(book_ratings.head())

#1. Print dataset size and examine column data types
print(book_ratings.shape[0])
print(book_ratings.dtypes)
#2. Distribution of ratings
print(book_ratings.value_counts())
#3. Filter ratings that are out of range
book_ratings = book_ratings[book_ratings["rating"]!= 0]
#4. Prepare data for surprise: build a Suprise reader object
from surprise import Reader
reader = Reader(rating_scale=(1, 5)) 
#5. Load `book_ratings` into a Surprise Dataset
from surprise import Dataset
data = Dataset.load_from_df(book_ratings[['user_id', 'book_id', 'rating']], reader)
#6. Create a 80:20 train-test split and set the random state to 7
from surprise.model_selection import train_test_split

trainset, testset = train_test_split(data, test_size=.2, random_state=42)
#7. Use KNNBasice from Surprise to train a collaborative filter
from surprise import KNNBasic

knn_basic = KNNBasic()
knn_basic.fit(trainset)
#8. Evaluate the recommender system
from surprise import accuracy
predictions = knn_basic.test(testset)
accuracy.rmse(predictions)

# 9. Prediction on a user who gave "The Three-Body Problem" a rating of 5
user_id = '8842281e1d1347389f2ab93d60773d4d'
item_id = '18245960'  # "The Three-Body Problem"

# Get the raw ID of the item
item_id_raw = book_ratings[book_ratings['book_id'] == int(item_id)]['book_id'].iloc[0]

# Get the predicted rating for the specified user and item
predicted_rating = knn_basic.predict(user_id, item_id_raw).est

print(f"The predicted rating for user {user_id} on the item {item_id} is: {predicted_rating}")

"""
#9. Prediction on a user who gave the "The Three-Body Problem" a rating of 5

user_id = '8842281e1d1347389f2ab93d60773d4d'
item_id = '18245960' #"18007564"

# Convert user and item ids to Surprise internal ids
trainset = data.build_full_trainset()
user_id_internal = trainset.to_inner_uid(user_id)
item_id_internal = trainset.to_inner_iid(item_id)

# Get the predicted rating for the specified user and item
predicted_rating = knn_basic.predict(user_id_internal, item_id_internal).est

print(f"The predicted rating for user {user_id} on the item {item_id} is: {predicted_rating}")


"""
