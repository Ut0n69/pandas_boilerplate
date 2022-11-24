import pandas as pd
from pandas import DataFrame

data = []


def main():
    df = pd.read_csv("./data/output.csv")
    df = DataFrame(df).rename(columns={
        0: 'open',
        1: 'high',
        2: 'low',
        3: 'close',
        4: 'volume',
        5: 'created_at'
    })

    print(df)


if __name__ == '__main__':
    main()
