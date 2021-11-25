![rinna](https://user-images.githubusercontent.com/81244428/143158931-37f15057-8ab3-4253-aa4f-923cc5f1a595.png)
# rinna with FastAPI

[rinna](https://huggingface.co/rinna/japanese-gpt2-medium)を使用した文章生成web APIをFastAPIを用いて構成しました。<br>


## API構成図
![rinnapi drawio](https://user-images.githubusercontent.com/81244428/143158868-3db19139-818d-48a2-9f02-9b857195dd42.png)
1. upload apiよりtextファイルをData storageのinputフォルダにアップロードする。
2. predict apiからfilenameを指定すると、非同期で以下のタスクを行う。<br>
――Data storageからtextファイルのダウンロード、Rinnaに入力、文章生成、outputフォルダにアップロード
3. download apiからfilenameを指定すると、生成された文章をoutputフォルダからダウンロードする。

## Usage
### Installation
デプロイする環境下で以下のコマンドを入力して下さい。
```
$ git clone https://github.com/Tyanakai/rinna_api.git
$ cd rinna_api
```
```
$ pip install -r requirements.txt
```
### Launch
起動するには以下のコマンドを入力して下さい。
```
$ uvicorn main:app
```
起動後、`127.0.0.1/docs`でSwagger UIを使用できます。

![swagger](https://user-images.githubusercontent.com/81244428/143162944-9bc40e0a-c9a5-4834-95cc-b3fd8f8e8b7d.PNG)

### Test
testsディレクトリ内の全てのテストケースを実行します。
```
$ python -m unittest discover tests
```
