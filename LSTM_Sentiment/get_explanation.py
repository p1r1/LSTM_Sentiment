import requests
import json
import sys

url = "https://www.uzaktangelir.com/admin/api.php"

payload = {
    'service': 'ProductsApi',
    'method': 'list',
    'username': 'bilgi@uzaktangelir.com',
    'password': '1q2w3e4r5t',
    'page': '1'
}

last_first_barcode = ""
j = 0
for i in range(1, 999111999):
    payload['page'] = f'{i}'
    # print(payload)
    response = requests.request("POST", url, data=payload)
    jsondata = json.loads(response.text.encode('utf8'))

    if not jsondata["data"] or not jsondata["data"][0]:
        print("data not found")
        sys.exit(0)

    # check if last page
    if last_first_barcode == jsondata["data"][0]["prd_barcode"]:
        print(f"{j} adet ürün\nAll Done!")
        break
    else:
        last_first_barcode = jsondata["data"][0]["prd_barcode"]

    text = ""
    for product in jsondata["data"]:
        if product:
            j = j + 1
            # print(product["prd_barcode"])
            if product["prd_meta_description"]:
                # print(product["prd_meta_description"])
                try:
                    text += product["prd_meta_description"] + "\n"
                except:
                    pass

        with open("D:\\prd_meta_description.txt", "a", encoding="utf-16") as myfile:
            myfile.write(text)
        text = ""
