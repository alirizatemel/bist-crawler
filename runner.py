import requests
import zipfile
import io
import datetime
import time
  
# sending get request and saving the response as response object

start_date = datetime.date(2019, 11, 18)
end_date = datetime.date(2015, 1, 1)
delta = datetime.timedelta(days=1)
token=1631212774454
print('='*15+" RUNNER START "+"="*15)
while start_date >= end_date:
    if start_date.weekday()<5:
        print("-"*45)
        print(start_date)
        year=str(start_date.year)
        month='{:02d}'.format(start_date.month)
        day='{:02d}'.format(start_date.day)
        if (month==1 and day==1) or (month==4 and day==23) or (month==5 and day==1) or (month==5 and day==19) or (month==8 and day==30) or (month==10 and day==29) or (month==7 and day==15):
            print('holiday')
        else:
            # ORIGINAL URL
            # URL = "https://borsaistanbul.com/data/thm/2021/09/thm202109071.zip?_=1631212774450"
            URL = "https://borsaistanbul.com/data/thm/"+year+"/"+month+"/thm"+year+month+day+"1.zip?_="+str(token)
            print("Download From ")
            print(URL)
            try:
                r = requests.get(url = URL,stream=True)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall('./bist-excels/')
                time.sleep(3);
            except:
                token += 1
                f = open("filesnotdownloaded.txt", "a")
                f.write(URL+"\n")
                f.close()
        
    start_date -= delta
    
