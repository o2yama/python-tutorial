# Python モジュール

### os 
#### OSとのやり取りする関数のモジュール
 print(os.getcwd()) #カレントディレクトリ
 os.chdir('../') #カレントディレクトリ変更
 os.system('mkdir NewDir') #システム側のシェルで実行

## shutil 
### ファイルやディレクトリ管理
 shutil.copyfile('game.py', 'game2.py')
 shutil.move('num_row.py', './NewDir/')

## glob
### ワイルドカード検索
 l = list(f for f in glob.glob('*.py'))  
 print(l) 

## re
### 高度な文字列処理を行う正規表現ツール
 print(re.findall(r'\b[bf][a-z]*', 'hey boy, which foot or hand fell fastest, bull sit'))

## math 
### 浮動小数点数数学用の下層ライブラリのCライブラリ関数にアクセス
 print(math.tan(2))
 print(math.log(1024, 2))

## random
 print(random.choice(list(i**2 for i in range(10)))) 
 print(random.sample(list(i**2 for i in range(10)), 8)) #重複なし
 print(random.random())
 print(random.randint(0, 20))

## urllib import response 
### 基本的な統計
 data = list(round(random.random(), 2) for i in range(8))
 print(data)
 print(statistics.mean(data)) #平均
 print(statistics.median(data)) #中央値
 print(statistics.variance(data)) #分散

## urllib.request import urlopen 
### インターネットアクセス
 with urlopen('https://google.com') as response:
     for line in response:
         line = line.decode('utf-8') #バイナリデータをテキストコードにデコード
         if 'EST' in line or 'EDT' in line: #東部標準時を返す
             print(line)

## datetime import date
 print(date.today())

##zlib 
### データの圧縮
 s = b'witch which has which whites wrist watch'
 print(len(s))
 print(zlib.compress(s))
 print(zlib.decompress(zlib.compress(s)))

## reprlib
## pprint
### 出力整形
 print(reprlib.repr(set('dsafdsfnajernbvgfiupernviopadsmveinrs')))

 data = [[[23,54,234],234,[543,2,1123,7]],756,12,[45,12,654,7,3,234],324,]
 pprint.pprint(data)

## from string import Template 
### 出力のテンプレート作成
 t = Template('${village} folk send $$10 to $cause')
 print(t.substitute(village='Japan', cause='the bitch fund'))

## import logging 
### ログとり
 logging.debug('Debigging information')
 logging.info('Info message')
 logging.warning('Warning: config file %s not found', 'server.conf')
 logging.error('Error occurred')
 logging.critical('Critical error -- shutting down')

## cat
### ファイル名を指定して読み取り
 cat requirements.txt

## decimal
### 十進数の計算を行うためのモジュール
https://www.fenet.jp/dotnet/column/tool/6705/
d1 = Decimal("0.1")
d2 = Decimal("0.2")
d3 = d1 + d2

print(f3) # 0.30000000000000004
print(d3) # 0.3
print(f3 == d3) # False


## 仮想環境（venv）

#### 環境生成
 python3 -m venv env-name

#### 実行
 . env-name/bin_activate

#### パッケージ管理 (pip)
##### 検索
pip search astronomy

##### コマンド種類
search, install, uninsatall, freeze

##### インストール 
python -m pip install packge-name (最新のバージョン)
python -m pip install packge-name==version-name (バージョン指定)

##### パッケージアップグレード
python -m pip install --upgrade packge-name

##### パッケージ削除
python -m pip uninstall package-name

##### パッケージ情報
pip show package-name

##### 環境にインストール済みのパッケージ
pip list

##### 使用パッケージの書き出し、共有
パッケージの書き出し
requirements.txtにセーブするのが一般的
pip freeze > requirements.txt

ユーザー側の読み込み
cat requirements.txt

すべてのパッケージのインストール
python -m install -r requirements.txt

## ドキュメント
#### python標準ライブラリ
https://docs.python.org/3/library/

#### pythonモジュールのインストール
https://docs.python.org/ja/3/installing/index.html

#### pythonメインサイト
https://www.python.jp/

#### Python CookBook
https://code.activestate.com/recipes/langs/python/

#### アルゴリズム
https://scipy.org/

#### 小数点の不思議
https://www.stat.cmu.edu/~brian/711/week03/perils-of-floating-point.pdf

