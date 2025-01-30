import json
import os
import argparse
from datetime import datetime
import sys

def extract_and_save_lines(json_file_path, keyword):
    """
    指定されたJSONファイルからlinesにkeywordが含まれる行を抽出し、
    titleとlines全文をテキストファイルとして出力します。
    createdで昇順ソートされます。

    Args:
        json_file_path (str): JSONファイルのパス
        keyword (str): 抽出する行に含まれるキーワード
    """

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"エラー: ファイル {json_file_path} が見つかりません。")
        return False
    except json.JSONDecodeError:
        print(f"エラー: ファイル {json_file_path} が正しいJSON形式ではありません。")
        return False

    # 抽出結果を一時保存するリスト
    extracted_data = []

    for page in data.get('pages', []):
        title = page.get('title', '')
        created = page.get('created', '')
        lines = page.get('lines', [])

        extracted_lines = []
        for line in lines:
            if keyword in line.get('text', ''):
                extracted_lines.append(line['text'])

        if extracted_lines:
            extracted_data.append({
                'created': created,
                'lines': lines
            })

    # createdで昇順ソート
    extracted_data.sort(key=lambda x: x['created'])

    output_file_path = os.path.join(os.getcwd(), 'output.txt')
    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for item in extracted_data:
                created_date = datetime.fromtimestamp(int(item['created'])).strftime('%Y-%m-%d %H:%M:%S')
                outfile.write(f"作成日：{created_date}\n")
                for line in item['lines']:
                    outfile.write(f"{line['text']}\n")
                outfile.write("\n")

    except Exception as e:
        print(f"エラー: ファイル {output_file_path} への書き込み中にエラーが発生しました: {e}")
        return False
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='JSONファイルからキーワードを含む行を抽出してテキストファイルに出力します。')
    parser.add_argument('json_file_path', type=str, help='JSONファイルのパス')
    parser.add_argument('keyword', type=str, help='抽出する行に含まれるキーワード #タグを抽出する場合はダブルクォーテーションで囲んでください')

    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        parser.print_help()
        sys.exit(1)

    if len(sys.argv) != 3:
        parser.print_help()
        sys.exit(1)

    if extract_and_save_lines(args.json_file_path, args.keyword):
        print(f"抽出結果を output.txt に保存しました。")