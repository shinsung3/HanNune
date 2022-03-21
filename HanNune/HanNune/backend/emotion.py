# import pandas as pd
# import jpype
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import seaborn as sns

# import warnings
# import re # 한국어 텍스트 데이터 전처리

# # 한국어 형태소 분석 - 명사 단위
# from konlpy.tag import Okt
# from collections import Counter
# import os
# from konlpy import utils
# from konlpy import jvm

# warnings.filterwarnings('ignore')
# df = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/tripadviser_review.csv")

# def apply_regular_expression(text): #한글만 뽑아내기
#     print(text)
#     hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 한글 추출 규칙: 띄어 쓰기(1 개)를 포함한 한글
#     result = hangul.sub('', text)  # 위에 설정한 "hangul"규칙을 "text"에 적용(.sub)시킴
#     return result

# # print(df.head())
# hotelText = df['text'][0]
# # print(apply_regular_expression(hotelText))
# # print(os.environ.get('JAVA_HOME'))
# print(os.getenv("JAVA_HOME"))
# # def main():
# # javadir = '%s%sjava' % (utils.installpath, os.sep)
# # args = [javadir, os.sep]
# # folder_suffix = ['{0}{1}open-korean-text-2.1.0.jar']
# # classpath = [f.format(*args) for f in folder_suffix]

# # print('javadir  : {}'.format(javadir))
# # print('os.sep   : {}'.format(os.sep))
# # print('classpath: {}'.format(classpath[0]))
# okt = Okt()  # 명사 형태소 추출 함수
# nouns = okt.nouns(apply_regular_expression(df['text'][0]))
# print(nouns)

# # if __name__ == '__main__':
# #     jvm.init_jvm()
# #     main()

from PyKomoran import *
komoran = Komoran("STABLE")
print(komoran)
print(komoran.get_plain_text("KOMORAN은 한국어 형태소 분석기입니다."))