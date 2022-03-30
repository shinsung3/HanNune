import os
from PyKomoran import Komoran, DEFAULT_MODEL
from collections import Counter
import wordcloud
import pandas as pd

import warnings

import pymysql

# def makeWordCloud(contents):
    
    # nlp = PyKomoran()
    # wordText=""
    # for t in contents:
    #     wordText += str(t) + " "
    
    # # 명사만 추출    
    # nouns = nlp.nouns(wordText)
    # # 추출
    # count = Counter(nouns)
    # wordInfo = dict()
    # # 가장 빈도수 높은거 100개만 고름
    # for tags, counts in count.most_common(100):
    #     if(len(str(tags)) > 1):
    #         wordInfo[tags] = counts
            
    # filename = os.path.join('/HanNune/backend/keyword', 'images/wordcloud01.png')        
    # taglist = pytagcloud.make_tags(dict(wordInfo).items())
    # pytagcloud.create_tag_image(taglist, filename, size = (800, 600), fontname = 'Korean', rectangular = False)     


# if __name__=="__main__":
#         print("")

conn = pymysql.connect(host='3.34.129.76',
                       user='hnune',
                       port=3306,
                       password='hannune',
                       db='hnune',
                       charset='utf8')

sql = "SELECT chat_cont FROM live_chat WHERE live_id = '1249'"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()

df = pd.DataFrame(result)
contents = df[0]

komoran = Komoran("EXP")
wordText=""
nouns=[]

for t in contents:
    nouns += komoran.get_morphes_by_tags(str(t), tag_list=['NNP', 'NNG', 'VA'])

stop_words = "!!! !! 당 상 듀 시네 시구 해주 신주 같 스 크 레 우 앙 링 리 오 슈 다 안 작 오 이용 용 드 아아 오오 녀"
stop_words=stop_words.split(' ')

word_result = []

for w in nouns:
    if w not in stop_words:
        word_result.append(w)

print(word_result)

# print(wordText)
# print(type(wordText))

# # 명사만 추출    
# nouns = komoran.get_nouns(wordText)
# nouns2 = komoran.nouns(wordText)
# print(nouns)
# print(nouns2)


# # 추출
word_count = Counter(word_result)
noun_list = word_count.most_common(100)

# cursor1 = conn.cursor(pymysql.cursors.DictCursor)

# insert_sql = "INSERT INTO 'live_keyword_rank' VALUES ('1249', max(keyword_rank)+1, %s, %s);"
# cursor1.execute(insert_sql, noun_list)
# conn.commit()

conn1 = pymysql.connect(host='3.34.129.76',
                       user='hnune',
                       port=3306,
                       password='hannune',
                       db='hnune',
                       charset='utf8')
cursor1 = conn1.cursor(pymysql.cursors.DictCursor)

for i in range(0,len(noun_list)):
    noun =[]
    noun.append('1249')
    noun.append(i+1)
    noun = noun + list(noun_list[i])
    print(noun)

    insert_sql = "INSERT INTO live_keyword_rank VALUES (%s, %s, %s, %s);"
    cursor1.execute(insert_sql, noun)
    
conn1.commit()
conn1.close()



# fontpath = 'H2GTRM.ttf'
# filename = os.path.join('', 'images\wordcloud01.png')        

# wordcloud = wordcloud.WordCloud(font_path=fontpath, background_color='white',max_font_size=100)
# wordcloud.generate_from_frequencies(dict(noun_list))
# wordcloud.to_file('wordcloud01.png')