from datetime import datetime
from datetime import timedelta
import requests
from pandas import DataFrame
from tqdm import tqdm

start = datetime.strptime('2020/05/25', '%Y/%m/%d')
end = datetime.strptime('2022/11/12', '%Y/%m/%d')
pair = 'btc_jpy'  # eth_jpy


def date_range(_start, _end):
    d = []
    for n in range((_end - _start).days):
        d.append(_start + timedelta(n))
    return d


data = []


def main():
    date_list = date_range(start, end)

    for i in tqdm(date_range(start, end), leave=False):
        date = f"{i.year}{i.month:02d}{i.day:02d}"
        response = requests.get(
            f"https://public.bitbank.cc/{pair}/candlestick/1hour/{date}")
        json_data = response.json()

        if not json_data["success"]:
            print("error: ", date)
            print(response)
            return

        for d in json_data["data"]["candlestick"][0]["ohlcv"]:
            append_data = d
            converted_date = datetime.fromtimestamp(append_data[5]/1000.0)
            append_data[5] = f"{converted_date.year}/{converted_date.month}/{converted_date.day} {converted_date.hour}:{converted_date.minute}"
            data.append(append_data)

    df = DataFrame(data)
    print(df)
    df.to_csv('./data/output.csv')


if __name__ == '__main__':
    main()
