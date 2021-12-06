import pandas as pd
import warnings

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
    keys = normalize_keys(compare_columns)
    A,B = normalize_columns(df_before, df_after)

    ensure_keys_exist(keys,A)
    ensure_keys_exist(keys,B)

    A = remove_dupes(compare_columns, A, "before")
    B = remove_dupes(compare_columns, B, "after")

    return A,B, keys


def ensure_keys_exist(keys,df):
    """ Ensure keys exist in columns of the dataframe"""
    if len(keys) == 0 :  
        raise ValueError(f"Key field {key} empty")
    columns = df.columns.values
    for key in keys:
        if key not in columns:
            raise ValueError(f"Key field {key} not in columns {columns}")
    return

def remove_dupes(compare_columns, df, name):
    """ Check if the dataframe has duplicate rows. And remove them. """
    duplicated_rows_in_df = df[df.duplicated(subset=compare_columns, keep=False)].shape[0]
    if duplicated_rows_in_df  :
        duplicated = str(df[df.duplicated(subset=compare_columns, keep=False)].to_dict(orient="records"))
        message_warning = f"Found {duplicated_rows_in_df} duplicated rows in {name} dataframe: " + duplicated + ". Removing duplicates, except last occurrente."
        warnings.warn(message_warning)
        df = df.drop_duplicates(subset=compare_columns, keep="last")
    return df

def normalize_columns(df_before : pd.DataFrame, df_after: pd.DataFrame) -> list:
    """ Ensure that the columns are the same in both df's. """
    A = df_before.copy()
    B = df_after.copy()



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

def normalize_keys(compare_columns) -> list :
    keys = []
    if isinstance(compare_columns, str):
        keys = compare_columns.split(",")
    elif isinstance(compare_columns, list):
        keys = compare_columns
    return keys


