# Data-Cleaning-Project---Trivia

This project was done using basic data manipulation skills, organized into a format ready for analysis in calculating scores.

The data is reshaped so that every column and question is a variable and that every row full of an individual trivia taker on each given date is an observation ready to be fed into statistical models.

Following the Python code, first, the initial CSV with 17,000+ data was read using pandas as a dataframe.

Then, the 'Correct' column indicating if a trivia taker got the question correct was changed from a string column to an integer column, with 1 representing Correct and 0 representing Not Correct (this is done in order for points to be tallied for score calculations).

The table is pivoted to allow for each column and question to be a variable (and their own column) using the now-integer values from the 'Correct' column. It is important to note that non-filled in values (NaN or Na) were declared as 'Incorrect', thus filled in as 0.

Finally, Raw Scores and Percentage Scores were calculated as their own columns into the dataframe, which is now finished and exported as a CSV.
