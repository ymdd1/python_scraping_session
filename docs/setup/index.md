# 事前準備

事前準備として、下記の作業をしていただきます。<br>
このページでは、主に開発環境作成に関して取り上げます。

- gitのインストール（割愛）
- githubアカウントの作成（割愛）
- エディタのインストール（割愛）
  - 特にこだわりがなければVSCodeがおすすめです。
- pythonのインストール（割愛）
  - インストールするpythonのバージョンは3系にしてください。今回は、python3.9.12を使用します。
  - お使いのマシンによっては、python2系がすでにインストールされている場合もあるので、ご注意ください。
- 事前学習
- 開発環境作成

# 事前学習

勉強会前に下記のサイトには目を通しておいてください。
`Google Colaboratory`を使って開発環境等を作らずともコードを書けるかと思います。
特に辞書型やリスト型に関する知識は必ず必要になります。

- [Python基礎の基礎](https://www.python.jp/train/type_and_func/index.html)
- [文字列と入出力](https://www.python.jp/train/string/index.html)
- [条件式と分岐](https://www.python.jp/train/if_condition/index.html)
- [ブール型と論理演算子](https://www.python.jp/train/logical_oper/index.html)
- [関数の定義](https://www.python.jp/train/function/index.html)
- [Pythonの型とオブジェクト](https://www.python.jp/train/list/index.html)
- [辞書](https://www.python.jp/train/dict/index.html)

# 開発環境作成

## pyenvのインストール&python3.9.12インストール

pyenvはpythonのバージョン管理ツールです。
nodeで言うところのnvmです。


[こちら](https://qiita.com/koooooo/items/b21d87ffe2b56d0c589b)を参考にpyenvのインストールをしてください。

インストールが終わったら、下記のコマンドを実行して、python3.9.12をインストールしてください。

```
// 下記のコマンドでインストール
$ pyenv install 3.9.12

// 下記のコマンドを実行して、3.9.12が表示されれば成功
$ pyenv versions

```

次に、バージョン3.9.12をグローバルに設定します。
これにより、ローカル全体でどこでもバージョン3.9.12を使うことができます。

```
$ pyenv global 3.9.12

// 下記コマンドで「Python 3.9.12」が表示されれば成功
$ python --version
```

## リポジトリをクローンする
githubにある今回のセッション用のリポジトリをクローンします。

今後は、そのリポジトリ内で開発をしていきます。<br>
下記のコマンドを実行してください。

```
$ git clone https://github.com/ymdd1/python_scraping_session.git
```

## 仮想環境を作成

仮想環境を作ることにより、このプロジェクトで行ったどんな変更も、あなたが開発している他のサイトに影響を及ぼさないようにすることができます。

具体的には、下記のような状況の際に、仮想環境は効果を発揮します。

基本的に、何か作る際には仮想環境を作るようにしましょう。

1. ひとつのシステム内で異なるPythonの環境（違うバージョンなど）を実行したい
2. プロジェクト単位でライブラリを管理したい


### 仮想環境作成コマンド

クローンをしたリポジトリ内の`codes`ディレクトリに入り、下記のコマンドを実行してください。

```
$ cd python_scraping_session/codes

// venvで仮想環境を作成します。ディレクトリにmyvenvフォルダが作られます。
$ python3 -m venv myvenv

// 下記のコマンドで仮想環境を立ち上げます。
$ source myvenv/bin/activate
```

※windowsの方は、[こちらのサイト](https://it-engineer-info.com/language/python/5545/)を参考にしてください。その際、仮想環境の名前は、`myvenv`にしてください。<br>

### 仮想環境が立ち上がっているか確認

`source myvenv/bin/activate`コマンドで仮想環境を立ち上げ、プロンプトの行頭に` (myvenv) `が付いたら、仮想環境(virtualenv) が起動されていることになります。

仮想環境の中で作業しているとき、python コマンドは自動的に正しいバージョンのPythonを参照するので、python3 コマンドの代わりに python コマンドを使うことができます。

仮想環境が立ち上がっているのを確認したら、`/codes`ディレクトリ内で下記のコマンドを実行。

```
$ python hello.py
```

実行後、下記のように`Hello! Take it easy`と表示されればOKです。

![take it easy](https://github.com/ymdd1/python_scraping_session/blob/main/docs/images/hello_py.png?raw=true) 

### 仮想環境の操作コマンド
下記のコマンドで仮想環境の立ち上げ・終了できます。<br>
仮想環境を立ち上げたまま他のプロジェクトを開発したりしないようにしましょう。

前項ですでに仮想環境を立ち上げているので、下記のコマンドを実行する必要はありません。

```
// 仮想環境を立ち上げる。※myvenvフォルダのある階層で行う。
$ source myvenv/bin/activate

// 仮想環境を終了。※myvenvフォルダのある階層で行う。
$ deactivate
```

### パッケージのインストール

仮想環境が立ち上がっているのを確認し、
下記のコマンドを実行してください。
実行する際は、`python_scraping_session/codes`ディレクトリにいることが必要になります。
```
$ pip install -r requirements.txt
```

上記のコマンドにより、`requirements.txt`ファイルに記述されているパッケージをローカル内にインストールします。

pip（ピップ）とは、プログラミング言語のPythonで開発されたパッケージを管理するためのパッケージ管理システムの一つで、Pythonに標準で含まれるため広く普及しています。nodeで言うところの`npm`になるかと思います。

pipを使うことは多いので、覚えておきましょう。

`pip install パッケージ名`でパッケージのインストールができます。

今回は、`requirements.txt`ファイルに記載したパッケージ群を一気にインストールするコマンドを実行しています。
詳しく知りたい方は[こちら](https://note.nkmk.me/python-pip-install-requirements/)を参照してください。