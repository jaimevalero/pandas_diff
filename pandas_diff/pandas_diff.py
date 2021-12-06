"""Main module."""
import pandas as pd
from pandas_diff.pre_process import pre_process
from pandas_diff.process_results import format_results_modify , format_results_create_delete

def get_diffs(before : pd.DataFrame, after: pd.DataFrame, keys: list, ignore_columns=[]):
    """ Generate DataFrame with differences between two DataFrames

    Args:
        before (pd.DataFrame): Before DataFrame
        after(pd.DataFrame): After DataFrame 
        keys (list): Key fields
        ignore_columns (list): Columns to not be considered for modify options (optional)
    """   
    results = []

    A,B = before, after

    A,B , keys = pre_process(A, B, keys)
    A["___keys"] = [ str(d) for d in A[keys].to_dict(orient="records") ]
    B["___keys"] = [ str(d) for d in B[keys].to_dict(orient="records") ]

    # Added elements are in B but not in A
    deleted_keys = list( set(A["___keys"].values ) -  set(B["___keys"].values ))
    # Deleted elements are in A but not in B
    added_keys = list( set(B["___keys"].values ) -  set(A["___keys"].values ))

    A = A.set_index('___keys')
    B = B.set_index('___keys')
    results = []


    for added_key in added_keys:
        result = format_results_create_delete(B.loc[added_key,:] ,"create",keys)
        results.append(result)

    for deleted_key in deleted_keys:
        result = format_results_create_delete(A.loc[deleted_key,:],"delete",keys)
        results.append(result)

    common_keys = list(set(A.index.values) & set(B.index.values))
    columns_not_keys = list(set(A.columns.values) - set(keys))

    for common_key in common_keys:
        for col in columns_not_keys:
            if col in ignore_columns: 
                continue
            # Check if the value has changed 
            are_different_non_null_values = A.loc[common_key,col] != B.loc[common_key,col] and not ( pd.isna(A.loc[common_key,col] ) and pd.isna(B.loc[common_key,col] ) )
            if are_different_non_null_values :
                result = format_results_modify(
                row = B.loc[common_key,:],
                keys = keys,
                attribute_changed = col,
                old_value = A.loc[common_key,col],
                new_value = B.loc[common_key,col]  )
                results.append(result)

    df = pd.DataFrame(results)
    return df


