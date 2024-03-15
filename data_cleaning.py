from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import pandas as pd

def fill_na_with_appropriate_value(df):
    """
    Fill NaNs with the column median for numeric variables and the mode for categorical variables.

    Parameters
    ----------
    df : DataFrame
        DataFrame with NaNs.

    Returns
    -------
    DataFrame
        DataFrame with previous NaNs set to column median for numeric variables and mode for categorical variables.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df_filled = df.copy()
    
    for column in df_filled.columns:
        # Check if the column is numeric
        if pd.api.types.is_numeric_dtype(df_filled[column]):
            median_value = df_filled[column].median()
            df_filled[column] = df_filled[column].fillna(median_value)
        else:
            # Assuming the column is categorical, fill with the mode
            # The mode could be empty, ensure there's at least one value
            mode_value = df_filled[column].mode()
            if not mode_value.empty:
                df_filled[column] = df_filled[column].fillna(mode_value[0])
    
    return df_filled


def separate_data(df, response):
    """
    Function to separate features and response variable

    Parameters
    ----------
    df: dataframe
        Dataframe containing true labels of groups (clusters)

    response: string
        String of column name of response variable
    Returns
    ----------
    X: df
        Dataframe containing features from dataset

    y: array-like, (n_samples,)
        Array containing the true labels for each data point
    """
    X = df.drop(response, axis=1)
    y = df[response]
    
    return(X, y)


def scale_data(df):
    """
    Function to scale numerical data

    Parameters
    ----------
    df: dataframe
        Dataframe containing true labels of groups (clusters)

    Returns
    ----------
    df_scaled: dataframe
        Dataframe containing scaled values of numeric variables
    """
    numeric_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(exclude=['number']).columns
    ct = ColumnTransformer([
        ('scale', StandardScaler(), numeric_columns)
    ], remainder='passthrough')

    # Fit and transform the data
    df_scaled_array = ct.fit_transform(df)
    
    # ColumnTransformer returns an array, convert it back to a DataFrame
    # Combine the column names for transformed and non-transformed columns
    all_columns = numeric_columns.tolist() + categorical_columns.tolist()
    df_scaled = pd.DataFrame(df_scaled_array, columns=all_columns, index=df.index)
    
    return df_scaled


def fill_na_column_median(df):
    """
    Fill NaNs with column median

    Parameters
    ----------
    df: df
        Dataframe with NaNs

    Returns 
    ----------
    df: df
        Dataframe with previous NaNs set to column median 
    """
    column_medians = df.median()
    df = df.fillna(column_medians)
    return df


def transform_categorical(df, categorical_vars):
    """ 
    Transform column into categorical variable 

    Parameters
    ----------
    df: df
        Dataframe containing columns to be transformed

    categorical_var: list
        List of column names to be transformed

    Returns
    df_copy: df
        Dataframe with transformed columns
    """ 
    df_copy = df.copy()

    for var in categorical_vars:
        df_copy[var] = df_copy[var].astype('category')
    
    return df_copy