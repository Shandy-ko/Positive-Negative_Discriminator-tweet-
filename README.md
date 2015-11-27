# Positive-Negative_Discriminator
これは、[単語感情極性対応表](http://www.lr.pi.titech.ac.jp/~takamura/pndic_en.html)(高村大也氏(東京工業大学))を利用して、ツイート毎の平均極性値と極性値の総計をグラフ化するプログラムです。　　

![図.1](/pic.png)

図.1のように青点が平均値、赤点が総計です。

## 仕組み
* 単語感情極性対応表(pn_ja.dic)を加工(pnnew.dic)してデータベース(pn.db)に保存
* load_tweet.pyで指定ユーザのタイムラインを読み込み
* mecab_requestdb.pyでツイート毎に形態素解析(mecab使用)をし、データベース問い合わせ
* pyplotで描画

## 問題点
* 対応表にない単語の極性値は0となる(類語であっても対応表になければ0となる ex)優れる→1.0,優位がある→0)
* 文脈のPN値を無視して単語のみで判定している
