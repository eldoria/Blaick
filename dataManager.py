import ZODB

# storage = ZODB.FileStorage.FileStorage('data/mydata.fs')
db = ZODB.DB('data/mydata.fs')
connection = db.open()
root = connection.root
