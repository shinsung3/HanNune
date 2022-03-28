import pymysql.cursors
import json

conn = pymysql.connect(
    host = "3.34.129.76", #ex) '127.0.0.1'
    port = 3306,
    user = "hnune",        #ex) root password = "password",
    password = "hannune",
    database = "HNUNE",
    charset = 'utf8'
)

curs = conn.cursor() #DB와 상호 작용을 위해 cursor 객체를 생성한다

with open('data/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
    data = json.load(f)
    # result = ['None','None']
    for i in range(0, len(data)):
        # print(data[i]['word'])
        sql = "INSERT INTO sentiword_info(word, word_root,polarity, id) VALUES (%s, %s, %s, %s)"
        val = (data[i]['word'], data[i]['word_root'], data[i]['polarity'], i)
        # if data[i]['word'] == wordname:
        #     result.pop()
        #     result.pop()
        #     result.append(data[i]['word_root'])
        #     result.append(data[i]['polarity'])
        curs.execute(sql, val)
        conn.commit()
    # r_word = result[0]
    # s_word = result[1]

# sql = "INSERT INTO sentiword_info(word, word_root,polarity, id) VALUES (%s, %s, %s)"
# val = ("1", "1","1")
# curs.execute(sql, val)
# conn.commit()

