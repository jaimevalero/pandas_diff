"""Console script for pandas_diff."""
import sys
import click
from pandas_diff import get_diffs
import pandas as pd



@click.command()
@click.option('--before',  help='Path to the before file. (.csv)' )
@click.option('--after',  help='Path to the after file. (.csv)' )
@click.option('--keys',  help='Keys to compare. (comma separated)' )





def load_dataframe(file: str)-> pd.DataFrame:
    """ Load a dataframe from """
    return pd.read_csv(file)
def main(before,after,keys):
    """Main function."""
    A = load_dataframe(before)
    B = load_dataframe(after)
    df = get_diffs(A,B,keys)
    print(df)

#def main(args=None):
#    """Console script for pandas_diff."""
#    click.echo("Replace this message by putting your code into "
#               "pandas_diff.cli.main")
#    click.echo("See click documentation at https://click.palletsprojects.com/")
#    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover



