import requests
import json
import time
import requests
import base64

while True:
    data = requests.get('https://visualisations.aemo.com.au/aemo/apps/api/report/ELEC_NEM_SUMMARY')
    aemo_data = json.loads(data.text)
    #print(aemo_data)

    region_data = aemo_data['ELEC_NEM_SUMMARY']
    #print(region_data)
    
    #region_in = input("Enter the region you want to get:(NSW1, QLD1, VIC1, SA1, TAS1) ")
    region_in = 'SA1'
    for region in region_data:
        if region['REGIONID'] == region_in:
            print("Displaying the data for region: "+region['REGIONID'])
            price = region['PRICE']
            demand = region['TOTALDEMAND']
            print("Price:  "+str(region['PRICE']))
            print("Demand: "+str(region['TOTALDEMAND']))
            
    text = ""
    if price < 0:
        text = "red"
    elif demand < 0:
        text = "green"
    elif demand > 1500:
        text = "yellow"
        
    if text != "":
        text1 = text.encode("ascii")
        text = base64.b64encode(text1)
        payload = {
            "payload_raw": text,
            "port": 1,
            "confirmed": False
        }
        text = requests.post('https://console.helium.com/api/v1/down/fa7b2bb7-a598-4b8d-880c-86713f64d4ab/mApsTRAIg4eb4Y4ClomfbY0Ka75_6kQC/dc1d764c-4542-4d51-b46e-4f52807015f0', data=payload)
        print(text)
    time.sleep(300)

#price -ve = blue
#demand > 1500 = red
#demand -ve = green
