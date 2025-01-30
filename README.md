# ex-cosenses
- Cosenseのjsonファイルからページをキーワード抽出してテキスト出力します。
- 動作環境はPython3です。
- 使い方は以下の通り
    1. CosenseのサイトからJsonをエクスポートします
    2. ex-cosenses.pyと同じフォルダに保存します
    3. 以下コマンドを実行します
    ```
    python3 ./ex-cosenses.py json_file_path keyword
    ```
    ```
    json_file_path  JSONファイルのパス
    keyword         抽出する行に含まれるキーワードです。#タグを抽出したい場合はキーワードをダブルクォーテーションで囲んでください。
    ```