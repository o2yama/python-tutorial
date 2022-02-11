from cmath import log
import imp
import os #OSとのやり取りする関数のモジュール

# print(os.getcwd()) #カレントディレクトリ
# os.chdir('../') #カレントディレクトリ変更
# os.system('mkdir NewDir') #システム側のシェルで実行

import shutil #ファイルやディレクトリ管理
# shutil.copyfile('game.py', 'game2.py')
# shutil.move('num_row.py', './NewDir/')

import glob
# l = list(f for f in glob.glob('*.py')) 
# print(l) 

import re #高度な文字列処理を行う正規表現ツール
# print(re.findall(r'\b[bf][a-z]*', 'hey boy, which foot or hand fell fastest, bull sit'))

import math #浮動小数点数数学用の下層ライブラリのCライブラリ関数にアクセス
# print(math.tan(2))
# print(math.log(1024, 2))

import random
# print(random.choice(list(i**2 for i in range(10)))) 
# print(random.sample(list(i**2 for i in range(10)), 8)) #重複なし
# print(random.random())
# print(random.randint(0, 20))

import statistics
from urllib import response #基本的な統計
# data = list(round(random.random(), 2) for i in range(8))
# print(data)
# print(statistics.mean(data)) #平均
# print(statistics.median(data)) #中央値
# print(statistics.variance(data)) #分散

from urllib.request import urlopen #インターネットアクセス
# with urlopen('https://google.com') as response:
#     for line in response:
#         line = line.decode('utf-8') #バイナリデータをテキストコードにデコード
#         if 'EST' in line or 'EDT' in line: #東部標準時を返す
#             print(line)

from datetime import date
# print(date.today())

import zlib #データの圧縮
# s = b'witch which has which whites wrist watch'
# print(len(s))
# print(zlib.compress(s))
# print(zlib.decompress(zlib.compress(s)))


# 出力整形
import reprlib
# print(reprlib.repr(set('dsafdsfnajernbvgfiupernviopadsmveinrs')))

import pprint
# data = [[[23,54,234],234,[543,2,1123,7]],756,12,[45,12,654,7,3,234],324,]
# pprint.pprint(data)

from string import Template # 出力のテンプレート作成
# t = Template('${village} folk send $$10 to $cause')
# print(t.substitute(village='Japan', cause='the bitch fund'))

import logging # ログとり
# logging.debug('Debigging information')
# logging.info('Info message')
# logging.warning('Warning: config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')


