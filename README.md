# MaBeeeMacApp

MaBeeeMacAppはMaBeeeをMacからコントロールできるようにするアプリです。UIを用意していないので開発者向けという感じです。[ツアー](https://github.com/novars-jp/MaBeeeMacApp/wiki/%E3%83%84%E3%82%A2%E3%83%BC)で雰囲気がわかります。

- [MaBeeeについてはこちらからどうぞ](http://mabeee.mobi/)


## 注意

- 現在のところMaBeeeはiOSアプリ、Androidアプリからの使用のみサポートされています。
- こちらのMacアプリは正式なサポート対象ではなく、あくまでMaBeee開発者の趣味レベルのものです。
- ご使用の際はその旨ご理解の上、自己責任でお願い致します。


## インストール・実行

1. このリポジトリをクローンなりダウンロードなりしてください。
1. MaBeeeMacApp.zipを解凍します。
1. 解凍してできたフォルダの中の、MaBeee.appがアプリになりますので、適当なところに置いてください。
1. 野良アプリなので署名がありません、実行するときは右クリックか2本指タップのコンテキストメニューから、「開く」を選んで実行してください。


## アイコン・終了

- 実行すると上部メニューバーの右側に、電池っぽいアイコンが表示されます。
- 電池アイコンをクリックして「Quit MaBeee」を選択すると終了できます。


## 仕組み・概要

1. 実行すると、``` http://localhost:11111/ ```でWebサーバーが起動します。
1. このWebサーバーにHTTP GETでリクエストを送信することで、アプリに指示を出します。
1. アプリは指示にしたがってMaBeeeをスキャンしたり出力を変更したりします。


## API

- HTTP GETでlocalhost:11111にリクエストを送信してください。
- ネットワーク経由で操作されないように、localhost, 127.0.0.1以外のホスト名、IPでアクセスできないようにしたつもりです。
- Access-Control-Allow-Origin "*" です。

| API (Path) | 概要 | リンク |
|:--|:--|:--|
| / | MaBeeeMacAppの状態のサマリを返します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/summary) |
| /state | Bluetoothの状態を返します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/state) |
| /scan | スキャンの状態を返します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/scan) |
| /scan/start | スキャンを開始します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/scan-start) |
| /scan/stop | スキャンを停止します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/scan-stop) |
| /devices | デバイスの一覧を返します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/devices) |
| /devices/:id | :idで指定したデバイスの情報を返します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/devices-:id) |
| /devices/:id/connect | :idで指定したデバイスに接続します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/devices-:id-connect) |
| /devices/:id/disconnect | :idで指定したデバイスを切断します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/devices-:id-disconnect) |
| /devices/:id/set | :idで指定したデバイスに値を設定します | [詳細](https://github.com/novars-jp/MaBeeeMacApp/wiki/devices-:id-set) |

## ツアー

APIを一通り使ってみる[ツアー](https://github.com/novars-jp/MaBeeeMacApp/wiki/%E3%83%84%E3%82%A2%E3%83%BC)を準備しました。


## ライブラリ

MaBeeeMacAppでは、Webサーバーの実装に[GCDWebServer](https://github.com/swisspol/GCDWebServer)を使用しています。素晴らしいライブラリに感謝します。
