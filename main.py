import time
import requests
import pandas as pd

with open("source.csv") as file:
    file_csv = pd.read_csv(file, encoding="utf-8")
    nameSeries = file_csv["Country Name"]
    urlSeries = file_csv["Image URL"]
    for i in range(len(urlSeries)):
        url = urlSeries[i]
        html_response = requests.get(url)
        with open("img/" + nameSeries[i]+".svg", mode="wb") as file:
            file.write(html_response.content)
        print('['+str(i+1)+'/'+str(len(urlSeries))+"]-"+nameSeries[i]+" has been downloaded.")
        time.sleep(1)
    print("All of items have been downloaded.")
