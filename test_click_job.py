import requests
import json

# 1) Prepare session
session = requests.Session()

# 2) Copy all the headers from your cURL (except the line breaks and the `\`)
headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "appid": "121",
    "authorization": "ACCESSTOKEN = eyJraWQiOiIzIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.…",
    "cache-control": "max-age=0",
    "clientid": "d3skt0p",
    "content-type": "application/json",
    "origin": "https://www.naukri.com",
    "referer": "https://www.naukri.com/job-listings-analyst-account-setup-check-adjustments-nlb-services-noida-new-delhi-delhi-ncr-0-to-0-years-270625010456?src=jobsearchDesk&sid=17519150868539803&xp=2&px=1&nignbevent_src=jobsearchDeskGNB",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "systemid": "jobseeker",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    # cookies go into session.cookies, not headers
}

# 3) Paste your cookie string exactly from cURL into session.cookies
cookie_pairs = """test=naukri.com; _t_s=seo; _t_sd=google; _t_r=1030%2F%2F; persona=default; ...; bm_sv=..."""
for pair in cookie_pairs.split("; "):
    name, value = pair.split("=", 1)
    session.cookies.set(name, value)

# 4) Build the JSON payload exactly as in --data-raw
payload = {
    "strJobsarr": ["270625010456"],
    "logstr": "--jobsearchDesk-2-F-0-1--17519150868539803-",
    "flowtype": "show",
    "crossdomain": True,
    "jquery": 1,
    "rdxMsgId": "",
    "chatBotSDK": True,
    "mandatory_skills": ["Accounting Operations", "Accounting"],
    "optional_skills": ["Cheque Fraud Adjustments", "Kyc Operations", "Aml Compliance"],
    "applyTypeId": "107",
    "closebtn": "y",
    "applySrc": "jobsearchDesk",
    "sid": "17519150868539803",
    "mid": ""
}

# 5) Send the request
url = "https://www.naukri.com/cloudgateway-workflow/workflow-services/apply-workflow/v1/apply"
resp = session.post(url, headers=headers, data=json.dumps(payload))

# 6) Check the result
print("Status code:", resp.status_code)
print("Response body:", resp.text)
if resp.status_code == 200 and "success" in resp.text.lower():
    print("🎉 Applied successfully via API!")
else:
    print("❌ Apply failed; please inspect status & body above.")
