import requests 
import json

endPoint = "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/Technology/30.json"
params={"api-key": "c351084de4f048a790d02911958fc6dd"}

def getNews():

    limit = 0
    message = ""
    news = []
    response = requests.get(endPoint,params)
    responseObj = json.loads(response.text)
    result = responseObj["results"]

    for i in range(len(result)):
        try:
            message = result[i]['title'] + "\n" +"Abstract: " + result[i]["abstract"] + "\n" + "url: "+result[i]["url"] + "\n\n"
            news.append(message)
            limit +=1
            if limit == 3:
                break
        except:
            pass
    return ''.join(news)