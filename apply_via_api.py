import requests

# 1) Prepare session
session = requests.Session()

# 2) Exact headers from DevTools (pure ASCII—no “…”!)
session.headers.update({
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "appid": "121",
    "authorization": "ACCESSTOKEN = <YOUR_FULL_ACCESS_TOKEN>",
    "cache-control": "max-age=0",
    "clientid": "d3skt0p",
    "content-type": "application/json",
    "origin": "https://www.naukri.com",
    "referer": "<YOUR_FULL_REFERER_URL>",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "systemid": "jobseeker",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
})

# 3) Set cookies from DevTools (split on '; ')
cookie_str = "<YOUR_FULL_COOKIE_STRING>"
for pair in cookie_str.split("; "):
    if "=" not in pair:
        continue
    name, value = pair.split("=", 1)
    session.cookies.set(name, value)

# 4) Payload exactly as in --data-raw (ASCII keys & values)
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

# 5) Send the request using json= so requests handles encoding
url = "https://www.naukri.com/cloudgateway-workflow/workflow-services/apply-workflow/v1/apply"
resp = session.post(url, json=payload)

# 6) Inspect results
print("Status code:", resp.status_code)
print("Response body:", resp.text)
if resp.status_code == 200 and "success" in resp.text.lower():
    print("🎉 Applied successfully via API!")
else:
    print("❌ Apply failed; inspect status & body above.")
