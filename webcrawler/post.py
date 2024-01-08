import requests
import json

def translate():
    paramas = {
        "from":'en'
    }
    data = {
        "kw":'car'
    }
    request = requests.post("https://fanyi.baidu.com/sug",data=data, params=paramas)

    print(request.json())
    

def translateInput():
    inputText = input("输入查询内容")
    data = {
        "kw":inputText
    }

    request = requests.post("https://fanyi.baidu.com/sug",data=data)

    print(request.json())
    
translateInput()