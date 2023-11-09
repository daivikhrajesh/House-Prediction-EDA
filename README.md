# House-Prediction-EDA

This Python toolkit provides a set of functions and classes for data preprocessing and visualization using pandas, numpy, seaborn, and matplotlib. 
The toolkit is designed to streamline the initial stages of data analysis, from loading datasets to visualizing patterns and performing basic mathematical operations.

## Contents

1. **`load_dataset(path)` Function**
   - Loads a CSV file as a pandas DataFrame.
   - Handles errors and returns None if loading fails.

2. **`Preprocessing` Class**
   - `datatypes(df)`: Returns the datatypes of each column.
   - `check_missing(df)`: Prints the number of missing values in each column.
   - `drop_unwantedCol(df, colname)`: Removes a specified column from the DataFrame.
   - `drop_null(df)`: Removes rows with missing values.
   - `duplicates(df)`: Removes duplicate rows.

3. **`Visualization` Class**
   - `boxplot(df, *args)`: Creates box plots based on specified columns.
   - `pairplot(df)`: Generates a pair plot for exploring relationships.
   - `heatmap(df)`: Plots a heatmap of the correlation matrix.
   - `scatterplot(df, *args)`: Creates scatter or box plots based on input arguments.

4. **`special_functions` Class**
   - `merge_2_dfs(df1, df2)`: Merges two DataFrames into a single DataFrame.
   - `slice_and_filter(df, colname, filter_val)`: Slices and filters a DataFrame.
   - `matrix_form(df)`: Converts DataFrame to a numpy array.
   - `df_with_condition(df, colname, operation, value)`: Filters DataFrame based on a specified condition.
   - `category(df, val)`: Groups DataFrame by a specified column.

5. **`math_functions` Class**
   - Provides basic mathematical functions for a given column in a DataFrame.
     - `min(df, colname)`: Prints the minimum value.
     - `max(df, colname)`: Prints the maximum value.
     - `mean(df, colname)`: Prints the mean value.
     - `median(df, colname)`: Prints the median value.
     - `std(df, colname)`: Prints the standard deviation.

## How to Use

1. Import the toolkit: `import data_preprocessing_visualization_toolkit as dpvt`.
2. Load your dataset: `data = dpvt.load_dataset('your_dataset.csv')`.
3. Use the classes and functions for data preprocessing and visualization.

## Dependencies
- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib

## Note
Ensure that you customize file paths and dataset specifics according to your project requirements. Report any issues or contribute to the toolkit's enhancement on GitHub.
