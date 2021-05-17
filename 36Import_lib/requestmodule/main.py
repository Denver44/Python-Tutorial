
import requests
# ------- This way we make get request ---------

r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)


# ------- This way we make post request ---------
# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
