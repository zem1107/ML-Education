# 教育用プロジェクト

Pythonのプログラムに慣れ親しむ目的で作成されたサンプルプログラムです。
WebアプリフレームワークとしてStreamlit、機械学習フレームワークとしてscikit-learnを使用します。

## 仕様

足の本数を入力すると、人か猫かを自動で判定して表示するアプリケーションです。

## 作成手順

プロジェクト直下に仮想環境を作成します。

```sh
$ python -m venv .venv
```

仮想環境にアタッチします。

```sh
$ . .venv/bin/activate
```

以下のライブラリをインストールします。

- streamlit
- scikit-learn

```sh
$ python -m pip install streamlit scikit-learn

# requirements.txtにまとめて記載する場合
# python -m pip install -r requirements.txt
```

streamlitのサンプルアプリを実行すると、デモアプリを見ることができます。

```sh
$ streamlit hello
```

app.pyを作成します

```python
import streamlit as st

st.title("Human or cat ?")

n_legs = st.number_input("足の本数", value=0)

if n_legs == 2:
    animal = "人間"
elif n_legs == 4:
    animal = "猫"
else:
    animal = "不明"

st.write('判定 ', animal)
```

作成したアプリを実行します。

```sh
$ streamlit run app.py
```

## デプロイ

[Pythonプロジェクト向けの.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)を作成します。


プロジェクトをGitリポジトリとしてリモートリポジトリにpushします。

```sh
$ git init
$ git add .  # VSCodeの画面操作で代替可能
$ git commit -m "first commit"  # VSCodeの画面操作で代替可能
$ git branch -M main
$ git remote add origin <REMOTE-URL>
$ git push -u origin main
```
