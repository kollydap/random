# from urllib import request, parse
import requests

# url = "http://127.0.0.1:8000"

# params = {
#     "first_name": "kolawole",
#     "last_name": "koladapo",
#     "email": "dapkolly@gmail.com",
#     "phone_number": "090837848930",
# }
# querystring = parse.urlencode(params)

# # u = request.urlopen(url + "?" + querystring)
# # resp = u.read()

# headers = {"User-agent": "none/ofyourbusiness", "Spam": "Eggs"}
# # v = request.Request(url, querystring.encode("ascii"), headers)
# url = "http://127.0.0.1:8000/api/v1/accounts/signup"
# resp = requests.post(url, data=params)
# # print(resp.cookies)
r = requests.get("http://httpbin.org/get?name=Dave&n=37")
