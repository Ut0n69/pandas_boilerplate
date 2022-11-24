from datetime import datetime
from pandas import DataFrame
import requests

data = []


def main():
    response = requests.get(
        "https://public.bitbank.cc/eth_jpy/candlestick/1month/2020")
    json_data = response.json()

    if not json_data["success"]:
        print(response)
        return

    for d in json_data["data"]["candlestick"][0]["ohlcv"]:
        append_data = d
        converted_date = datetime.fromtimestamp(append_data[5]/1000.0)
        append_data[5] = f"{converted_date.year}/{converted_date.month}/{converted_date.day} {converted_date.hour}:{converted_date.minute}"
        data.append(append_data)

    df = DataFrame(data)
    df.to_csv('./data/output.csv')

    print("\n create data successfully\n")


if __name__ == '__main__':
    main()
