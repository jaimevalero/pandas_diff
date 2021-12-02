"""Main module."""
import pandas as pd

def pre_process(df_before: pd.DataFrame , df_after: pd.DataFrame, compare_columns):
    """
    Pre-process the dataframe.

    Parameters
    ----------
    df_before : pandas.DataFrame
        The dataframe to pre-process.
    df_after : pandas.DataFrame
    Returns
    -------
    pandas.DataFrame
        The pre-processed dataframe.
    """
    A,B = normalize_columns(df_before, df_after, compare_columns)


    # Remove the index column
    #df = df.reset_index(drop=True)

    # Remove the column with the index
    #df = df.drop(columns=['index'])

    return

def normalize_columns(df_before, df_after, compare_columns):
    """ Ensure that the columns are the same in both df's. """
    A = df_before.copy()
    B = df_after.copy()

    keys = []
    if isinstance(compare_columns, str):
        keys.append(compare_columns)
    elif isinstance(compare_columns, list):
        keys = compare_columns

    # Check if the dataframes have the same columns.
    are_columns_different = not A.columns.equals(B.columns)
    if are_columns_different:
        columns_only_in_A = list(set(A.columns) - set(B.columns))
        columns_only_in_B = list(set(B.columns) - set(A.columns))

        for c in columns_only_in_A:
            B[c] = None
        for c in columns_only_in_B:
            A[c] = None

    return A,B

A = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5]})
B = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'C': [1, 2, 4, 4, 5]})

pre_process(A, B, ['A'])
