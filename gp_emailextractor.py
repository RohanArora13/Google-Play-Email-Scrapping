import urllib.request
import re,time

s1=time.time()
# some variable for filtering 
app_with_download_more_than = 10000
app_updated_after=["year":"2016","date":"1","month":"02"]


def linker(mainlink):
    mlink= urllib.request.urlopen(str(mainlink))
    page=mlink.read()
    #print (page)
    link=re.findall('href="/store/apps/details?(.*?)"',str(page),re.DOTALL)
    no=0
    for i in range(len(link)):
        #print link
        if(len(link[i])<100):
            if(link[i]>link[i-1]):
                #print (link[i])
                pagelink="https://play.google.com/store/apps/details"+str(link[i])
                #print (pagelink)
                mlink= urllib.request.urlopen(pagelink)
                appage=str(mlink.read())
                
                data2=re.findall('<span class="htlgb"><div class="IQ1z0d"><span class="htlgb">(.*?)</span></div></span></div><div class="hAyfc"><div class="BgcNfc">',str(appage))
                ## date
                ## print("date ="+data2[0])
                ## downloads
                #print("no of download ="+data2[2])

                data2=str(data2[2]).replace(",","").replace("+","")
          
                if(int(data2)>=app_with_download_more_than):

                    mail=re.findall('class="hrTbp euBY6b">(.*?)</a>',appage,re.DOTALL)
                    print (mail[0])
                    linker("https://play.google.com/store/apps/details"+str(link[i]))
                else:
                	None
                                

## starting link for extractor 
linker("https://play.google.com/store/search?q=cal&c=apps&price=1")
s2=time.time()

## timer
print (s2-s1)       

