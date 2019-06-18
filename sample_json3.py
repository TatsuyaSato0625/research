import json
import requests
import pymongo
#dataが四角のやつとツイートを含む、locateが四角,tweetがデータを表すグローバル変数
datas = {"datas":{"tweets":{},"locate":{}}}
location = []

#範囲内のデータの数
def range_datas_quantities(x0,x1,y0,y1,json_data):
    keyList = json_data.keys()
    i = 0
    for name in keyList:
        if((x0<=json_data[name]["lon"]<=x1) and (y0<=json_data[name]["lat"]<=y1)):
            i+=1
    return i


#範囲内のデータを返す
def range_datas(x0,x1,y0,y1,json_data):
    indatas={}
    keyList = json_data.keys()
    #valList = json_data.values()
    for name in keyList:
        if((x0<=json_data[name]["lon"]<=x1) and (y0<=json_data[name]["lat"]<=y1)):
            #nameがあるため、上書きされずに済んでいる
            indatas[name] = {
                    'lon':json_data[name]["lon"],
                    'lat':json_data[name]["lat"]
                    }


    #print(indatas)
    return indatas

#ツイート情報の必要な部分だけ抜きとる関数
def regist_tweets_part(json_data):
    indatas=[]
    keyList = json_data.keys()
    #valList = json_data.values()
    for name in keyList:
        indatas.append ({
                "key":name,
                'lon':json_data[name]["lon"],
                'lat':json_data[name]["lat"]
                }
                )
    #print(indatas)
    return indatas

#四分木
def four_devide_tree(x0,x1,y0,y1,json_data):
    #keyList = json_data.keys()
    if((range_datas_quantities(x0,x1,y0,y1,json_data))<=1):
        d1 = range_datas(x0,x1,y0,y1,json_data)
        d1 = regist_tweets_part(d1)
        location.append({
    #    'name':name,
    #    'lon':json_data[name]["lon"],
    #    'lat':json_data[name]["lat"],
        'x0':x0,
        'x1':x1,
        'y0':y0,
        'y1':y1,
        'width':x1-x0,
        'height':y1-y0,
        "tweets":d1
        })
        #print(location)
    else:
        #左下
        ld=range_datas(x0,(x1+x0)/2,y0,(y1+y0)/2,json_data)
        four_devide_tree(x0,(x1+x0)/2,y0,(y1+y0)/2,ld)
        #左上
        lu=range_datas(x0,(x1+x0)/2,(y0+y1)/2,y1,json_data)
        four_devide_tree(x0,(x1+x0)/2,(y0+y1)/2,y1,lu)
        #右下
        rd=range_datas((x0+x1)/2,x1,y0,(y1+y0)/2,json_data)
        four_devide_tree((x0+x1)/2,x1,y0,(y1+y0)/2,rd)
        #右上
        ru=range_datas((x0+x1)/2,x1,(y0+y1)/2,y1,json_data)
        four_devide_tree((x0+x1)/2,x1,(y0+y1)/2,y1,ru)

#番号をデータにふる
def regist_location_number(location):
    indatas = []
    for t in range(len(location)):
        indatas.append({
    #    'name':name,
    #    'lon':json_data[name]["lon"],
    #    'lat':json_data[name]["lat"],
        'number':t,
        'x0':location[t]["x0"],
        'x1':location[t]["x1"],
        'y0':location[t]["y0"],
        'y1':location[t]["y1"],
        'width':location[t]["width"],
        'height':location[t]["height"],
        'tweets':location[t]["tweets"]
        }
        )
    return indatas

def main():
    f = open("test2.json", 'r')
    #lonが経度, latが緯度
    json_data = json.load(f) #json形式で読み込む
    #print("{}", json.dumps(json_data,sort_keys = True, indent = 4)) json形式のデータプリント
    keyList = json_data.keys()
    #print("{}", keyList) ABCD....
    valList = json_data.values()
    #print(valList) #全ての緯度と経度
    #print(len(valList)) 緯度と経度の組み合わせが26個あると確認できる
    #range_datas(0,50,50,100,json_data)
    #print(json_data)
    #d1 = regist_tweets_part(json_data)
    four_devide_tree(0,100,0,100,json_data)
    d2 = regist_location_number(location)
    #print(location)
    #print(len(location))
    #print(json.dumps(location, indent =2))
    #datas["datas"]["tweets"]=d1
    #datas["datas"]["locate"]=d2
    #print(datas)
    #print(location[1]["y1"])
    #print(json.dumps(location,indent = 2))
    #print(json.dumps(d1, indent =2))
    print(d2)
    #print(valList["lon"])
    #print(datas)
    #print(json.dumps(datas, indent =2))
    """
    client = pymongo.MongoClient(host='localhost',port=50625)
    col = client['ex3']['locate']
    col.insert_many(d2)
    """
    #print(col.find_one())
"""
    for a in valList:
        print(a)
    for name in keyList:
        pass
        #print((1+json_data[name]["lon"])/2) 演算できることを確認
    t = range_datas_quantities(0,70,0,50, json_data)
    #print(t)
"""
"""
    name_list = ["honoka","eri","kotori","umi","rin","maki","nozomi","hanayo","niko"]
    for name in name_list:
        print("{0:6s} 身長：{1}cm BWH: ".format(name,json_data[name]["height"]),end="\t")
        #{0:6s}にname,{1}に.json_data[name]["height"]
        for i in range(len(json_data[name]["BWH"])):
            #range(len())でlenで図った長さ分繰り返してる。
            print("{}".format(json_data[name]["BWH"][i]),end="\t")
        print()
"""

if __name__=='__main__':
    main()
