import requests,re
rijecisa5=re.findall(r"\n[a-z]{5}\n",str(requests.get("https://raw.githubusercontent.com/vido89/Liste-srpskih-rijeci/master/pdf.dic").text))
arrayrijeci=[]
for x in rijecisa5:
    arrayrijeci.append(x.replace("\n",""))
print(arrayrijeci)