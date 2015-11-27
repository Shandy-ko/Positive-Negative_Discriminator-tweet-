# coding: utf-8
import MeCab
import re
import sqlite3
import matplotlib.pyplot as plt
import test2 as lt


if __name__ == "__main__":
  values = []
  avg = []
  connector = sqlite3.connect("pn.db")
  connector.text_factory = str
  cursor    = connector.cursor()


  mt = MeCab.Tagger("mecabrc")

  for tweet in lt.tweets:
    res = mt.parseToNode(tweet)

    morphs = []
    readings = []
    while res:
      if not re.match(res.feature, "BOS/EOS"):
        arr = res.feature.split(",")
        morphs.append(arr[-3])
        readings.append(arr[-2])
      res = res.next

    sum = 0
    value = []
    i = 0
    while i < len(morphs):

      word = morphs[i]
      reading = readings[i]
      searchs = (word,reading)
      words = (word,)
      cursor.execute("select * from pndic where word=? and yomi=?", searchs)
      result = cursor.fetchall()

      if len(result) == 0:
        cursor.execute("select * from pndic where word=?", words)
        result = cursor.fetchall()

      for row in result:
        value.append(row[2])

      for val in value:
        sum += val

      i +=1

      a = len(value)
    values.append(sum)
    if a == 0:
      avg.append(0)
    else:
      avg.append(sum/a)

  cursor.close()
  connector.close()

  print values
  print avg

plt.axhline(y=0, c='gray')
plt.plot(lt.dates,values, c='red', marker="o")
plt.plot(lt.dates,avg, c='blue', marker="o")
plt.show()
