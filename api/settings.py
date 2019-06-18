MONGO_URI = 'mongodb://localhost:50625/ex3'  # 接続先MongoDBの //ドメイン:ポート番号/DB名
X_DOMAINS = '*'               # このAPIへのアクセス許可ドメイン
HATEOAS = False               # Restfulの拡張
PAGINATION = False            # ページ送り
URL_PREFIX = 'api'            # このAPIのURL接頭辞 http://localhost:50503/api
DOMAIN = {'locate':{    # 公開するmongodbコレクション名
    'item_title': 'locate',  # 返されるjsonファイルにおけるkey
    'url':'locate',          # 公開用のURL http://localhost:50503/api/locate
    'schema':{
        'number':{'type':"integer"},
        'x0':{'type':'float'},  # 以降，jsonファイルに含めるmongodbのフィールド(キー)名と型
        'x1':{'type':'float'},
        'y0':{'type':'float'},
        'y1':{'type': 'float'},
        'width':{'type':'float'},
        'height':{'type':'float'},
        'tweets':{}
            }
        }
    }
