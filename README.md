# Book Recommender System

This project aims to develop a book recommender system for Books’R’Us, a national bookstore chain, using the Surprise library. The recommender system utilizes collaborative filtering techniques to provide personalized book recommendations to users based on their past ratings and preferences.

## Tasks Completed
- [x] Prepare data for recommender implementation
- [x] Examine dataset statistics and data types
- [x] Filter out ratings not in the range of 1 to 5
- [x] Build a Surprise reader object with the established rating scale
- [x] Load book_ratings into a Surprise Dataset
- [x] Split the data into training and test sets
- [x] Train a collaborative filter using KNNBasic algorithm
- [x] Calculate the RMSE of the trained recommender system
- [x] Predict the rating for a specific book based on user data
- [x] Fine-tune hyperparameters to optimize the collaborative filter

## Files Included
- **Goodreads_ratings.csv**: Dataset containing user ratings for books
- **solution.py**: Python script containing the implementation of the book recommender system
- **script.py**: Python script providing the final results and recommendations

## Usage
1. Ensure Python and necessary libraries (such as Surprise) are installed.
2. Clone or download the repository containing the project files.
3. Run the `script.py` file to execute the recommender system and view the results.

## Results
The recommender system successfully predicts user ratings for books and provides personalized recommendations based on collaborative filtering techniques. The RMSE of the trained model indicates its effectiveness in predicting user preferences.

## Further Improvements
To enhance the recommender system:
- Experiment with different collaborative filtering algorithms and hyperparameters to improve accuracy.
- Incorporate additional features, such as book genres or user demographics, for more accurate recommendations.
- Implement user interface for interactive usage and seamless integration with the Books’R’Us website.


Feel free to contribute to the project by suggesting improvements or reporting issues. Happy recommending!