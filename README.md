# 概要
[Paul Kart]()で利用できるWebSocketコントローラのサンプルです。

## 内容
- WebSocketController: Pythonを用いたPID制御器の実装例です。
- WebSocketMATLABController: WebSocketサーバとしてのみPythonを利用し、バックエンドでMATLABのAPIをコールする実装例です。

# 使い方
依存ライブラリを適宜インストールしたうえで、server.pyを実行してください。制御系のカスタマイズの際には主に以下のファイルを編集してください。

- server.py: WebSocketの受付ポート設定など。制御器のインスタンスもここで持っているのでパラメータ設定の際にも編集。
- pid_controller.py/PIDController.m: 制御器の構造を変える場合はこちら。
- player_input_manager.py: プレイヤーからのキーボード入力を変更する場合はこちら。
