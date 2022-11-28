# おさらい+α

## 辞書型

辞書に含まれる要素はキーと値の組み合わせとなっており、キーを指定することで対応する値を取得することができます。

### 辞書型の取り出し

```python
mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}

print(mydict["DE"])
>> Germany
print(mydict["FR"])
>> France
print(mydict["JP"])
>> Japan
```

なお存在しないキーを指定すると KeyError エラーが発生します。

```python
mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}
print(mydict["BR"])

>> Traceback (most recent call last):
>>   File "<stdin>", line 1, in <module>
>> KeyError: 'BR'
```

#### getメソッドを使用して値を取得する

キーを指定して値を取得するのは同じですが、存在しないキーを指定した場合にはデフォルト値を返す方法です。辞書型で利用可能な get メソッドを使用します。

```python
mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}

print(mydict.get("DE"))
>> Germany
print(mydict.get("EN"))
>> None
print(mydict.get("EN", "NotFound"))
>> NotFound
```

## 配列型

リスト内包表記と呼ばれる記述方法をご紹介します。

### 1行で書くリスト処理

今回は以下の配列データを扱うこととします。
```python
data = [1, 2, 3, 4, 5]
```

この配列について、各要素の値を2倍にする処理を通常のfor文で記述すると、以下のようになります。
```py
# data配列の中身を2倍にする
newData = []
for d in data:
  newData.append(d * 2)
```  

この3行の実装を、リスト内包表記で記述すると1行で記述することができます。
```py
# data配列の中身を2倍にする
newData = [d * 2 for d in data]
```

この書き方はシンプルだし直感的に理解できるので、なかなか便利です。

### 1行で書くリスト処理（if文付き）
さらに、処理の中で条件式（if文）を記述することもできます。

例えば偶数のみ処理したい場合に、通常の書き方では以下のように記述します。
```py
newData = []
for d in data:
    if d % 2 == 0:
        newData.append(d * 2)     
```
上記の場合には4行の実装ですが、リスト内包表記だと以下のように1行で記述することができます。
```py
newData = [d * 2 for d in data if d % 2 == 0]
```


