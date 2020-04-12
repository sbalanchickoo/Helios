import csv
import sys
import pandas as pd


def get_csv(path: str) -> list:
    with open(path) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]
    return a


def get_csv_pandas(path: str) -> list:
    """Form a complex number.

    Parameters:
    real (int): The real part (default 0.0)

    Returns:
    int:Returning value

    """
    df = pd.read_csv(path)
    df_list = df.to_dict('records')
    return df_list


if __name__ == '__main__':
    file_path = sys.argv[1]
    csv_content = get_csv_pandas(file_path)
    print(csv_content)
    # print(sys.argv[1:])
