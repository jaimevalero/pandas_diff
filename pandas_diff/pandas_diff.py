"""Main module."""
import pandas as pd
from pre_process import pre_process
from process_results import format_results_modify , format_results_create_delete
import click

#A = pd.DataFrame([{"hero" : "hulk" , "power" : "strength", "false_key" : "1"},
#                  {"hero" : "black_widow" , "power" : "spy" , "false_key" : "2"},
#                  {"hero" : "thor" , "hammers" : 0 , "false_key" : "3" },
#                  {"hero" : "thor" , "hammers" : 1 ,  "false_key" : "4"} ] )
#B = pd.DataFrame([{"hero" : "hulk" , "power" : "smart",  "false_key" : "1"},
#                 {"hero" : "captain marvel" , "power" : "strength",  "false_key" : "5"},
#                 {"hero" : "thor" , "hammers" : 2 ,  "false_key" : "3"} ] )
#A,B , keys = pre_process(A, B, ["hero","false_key"])


#A["___keys"] = A[keys]
#B["___keys"] = B[keys]


@click.command()
@click.option('--before',  help='Path to the before file. (.csv)' )
@click.option('--after',  help='Path to the after file. (.csv)' )
@click.option('--keys',  help='Keys to compare. (comma separated)' )

def load_dataframe(file: str)-> pd.DataFrame:
    """ Load a dataframe from """
    return pd.read_csv(file)

def get_diffs(before : pd.DataFrame, after: pd.DataFrame, keys: list):
    """[Generate DataFrame with differences between two DataFrames]

    Args:
        A (pd.DataFrame): [Before DataFrame]
        B (pd.DataFrame): [After DataFrame ]
        keys (list): [description]
    """    """ Get the diffs between two dataframes."""
    results = []

    A,B = before, after

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

def main(before,after,keys):
    """Main function."""
    A = load_dataframe(before)
    B = load_dataframe(after)
    df = get_diffs(A,B,keys)
    print(df)

#if __name__ == '__main__':
#    #main()
#    a=0




if __name__ == '__main__':
    unittest.main()
