import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_dataset(path):
    """
    Load a CSV file as a pandas DataFrame.

    Parameters:
    path : str
        The file path of the CSV file to be loaded.

    Returns:
    pandas.DataFrame
        The pandas DataFrame containing the data from the CSV file.

    Exception:
        If an error occurs while loading the CSV file, this function will print
        the error message and return None.
    """
    try :
        dataframe=pd.read_csv(path)
        return dataframe
    except Exception as e:
        print(e)

class Preprocessing:
    """
    A class for performing data preprocessing operations on a pandas DataFrame.
    """

    def datatypes(df):
        """
        Args:
            df (DataFrame): The input DataFrame.

        Returns:
            pandas Series: A Series containing the datatypes of each column.
        """

        return df.dtypes

    def check_missing(df):
        """
        Prints the number of missing values in each column of the input DataFrame.

        Args:
            df (pandas DataFrame): The input DataFrame.
        """
        print(df.isnull().sum())

    def drop_unwantedCol(df, colname):
        """
        Removes a specified column from the input DataFrame and returns the modified DataFrame.

        Args:
            df (pandas DataFrame): The input DataFrame.
            colname (str): The name of the column to be removed.

        Returns:
            pandas DataFrame: The modified DataFrame with the specified column removed.
        """
    def drop_unwantedCol(df, colname):
        try:
            df2 = df.copy()
            df2.drop([colname], axis=1, inplace=True)
            print('{} is removed'.format(colname))
            return df2
        except Exception as e:
            print(e)

    def drop_null(df):
        """
        Removes all rows containing missing values from the input DataFrame.

        Args:
            df (pandas DataFrame): The input DataFrame.
        """
        df.dropna(how = 'any') 

    def duplicates(df):
        """
        Removes duplicate rows from the input DataFrame.

        Args:
            df (pandas DataFrame): The input DataFrame.
        """
        df3 = df.copy()
        duplicate_rows_df = df[df3.duplicated()]
        print("number of duplicate rows: ", duplicate_rows_df.shape[0])
        if duplicate_rows_df.shape[0] == 0:
            print('No duplicate Rows found')
        else: 
            df.drop_duplicates(inplace = True)

class Visualization:
    """
    A class for creating visualizations from a pandas DataFrame.
    """

    def boxplot(df, *args):
        """
        Creates a box plot from the input DataFrame.

        Args:
            df (pandas DataFrame): The input DataFrame.
            *args: The columns to use for creating the plot. If one column is specified,
                   creates a single plot.

        Returns:
            matplotlib axes: The axes of the created plot.
        """
        try:
            if len(args)==1 :
                ax = sns.boxplot(x=df[args[0]])
            else: 
                ax = sns.boxplot(x=df[args[0]], y=df[args[1]] )
            plt.show()
        
        except Exception as e:
            print(e)


    def pairplot(df):
        """
    Plot pairwise relationships in a dataset.

        The input dataset for which to plot pairwise relationships.

        The function generates a visualization but does not return anything.
    """
        sns.pairplot(data = df)

    def heatmap(df):
        """
    Plot a heatmap of the correlation matrix for a given dataset.

        The input dataset for which to plot the heatmap of the correlation matrix.

        The function generates a visualization but does not return anything.
    """
        c = df.corr()
        sns.heatmap(c)


    def scatterplot(df, *args):
        """
    Plot a scatter or box plot based on the input arguments.

    The input dataset for which to plot the scatter or box plot.

    *args : tuple
        The input arguments for the scatter or box plot. If there are two arguments, a scatter plot
        will be created with the first argument as the x-axis and the second argument as the y-axis.

        The function generates a visualization but does not return anything.

    Exception:
        If an error occurs while plotting the scatter or box plot, this function will print
        the error message and return None.
    """
        try:
            if len(args)==2 :
                ax = sns.scatterplot(x=df[args[0]], y=df[args[1]])
            else: 
                ax = sns.boxplot(x=df[args[0]], y=df[args[1]], hue=df[args[2]] )
            plt.show()
        
        except Exception as e:
            print(e)


class special_functions:
        def merge_2_dfs(df1, df2):
            """
    Merge two pandas DataFrames into a single DataFrame.

   
    df1 : The first pandas DataFrame to merge.

    df2 : The second pandas DataFrame to merge.


    The function merges the two input DataFrames and prints the merged DataFrame.

    Exception:
        If an error occurs while merging the two DataFrames, this function will print
        the error message and return None.
    """
            try:
               # df1.merge(df2)
                concat_df = pd.concat([df1, df2], axis=1)

                print(concat_df)
                #print("After Merging:\n ",df1)
            except Exception as e:
                print(e)



        def slice_and_filter(df, colname, filter_val):
            """
    Slice and filter a pandas DataFrame based on a given column name and value.

    df : The input DataFrame to slice and filter.

    colname : The name of the column in the DataFrame to filter.

    filter_val : The value to filter the column by.


    The function filters the input DataFrame based on the given column name and value and
    prints the resulting filtered DataFrame.

    Exception: 
        If an error occurs while slicing and filtering the DataFrame, this function will print
        the error message and return None.
    """
            try:
                print(df[df[colname] == filter_val])
            except Exception as e:
                print(e)


        def matrix_form(df):
                """
    Converts a pandas DataFrame into a numpy array.

    
    df : The DataFrame to be converted.

    Returns: A numpy array representation of the DataFrame.

    Exception:
        If the input is not a valid pandas DataFrame.
        """
                try:
                    data=df.to_numpy()
                    return data
                except Exception as e:
                    print(e)
            

        def df_with_condition(df, colname, operation, value):

            """
    Filters a pandas DataFrame based on a specified condition.

    
    df : The DataFrame to be filtered.
    colname : str
        The name of the column to filter on.
    operation : str
        The comparison operator to use. 
    value : int or str
        The value to compare against.

    Return: The function prints the filtered DataFrame to the console.

    Exception:
        If the input is not a valid pandas DataFrame or if the operation is not a valid comparison operator.

    """
            try:
                if operation == '<':
                    print(df[df[colname]<value])
                elif operation == '>':
                    print(df[df[colname]>value])
                elif operation == '=':
                    print(df[df[colname]==value])
                elif operation == '!=':
                    print(df[df[colname]!=value])
            except Exception as e:
                print(e)


         
        def category(df, val):
            try:
                print(df.groupby([val]))
                
            except Exception as e:
                print(e)
            
      
    
class math_functions:
    """
math_functions - A class that provides basic mathematical functions for a given column in a pandas DataFrame.

Attributes:
    df : The input DataFrame.
    colname (str): The name of the column to perform the mathematical functions on.

Methods:
    min(): Prints the minimum value of the column specified by colname.
    max(): Prints the maximum value of the column specified by colname.
    mean(): Prints the mean value of the column specified by colname.
    median(): Prints the median value of the column specified by colname.
    std(): Prints the standard deviation of the column specified by colname.
"""        
    def min(df, colname):
        print(np.min(df[colname]))
              
    def max(df, colname):
        print(np.max(df[colname]))
              
    def mean(df, colname):
        print(np.mean(df[colname]))
      
    def median(df, colname):
        print(np.median(df[colname]))
    
    def std(df, colname):
        print(np.std(df[colname]))
        