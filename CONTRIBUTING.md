# Contributing to ChatGPT Pro 無料 Open Source Codex OSS

ありがとうございます！このプロジェクトへの貢献は歓迎します。

## ルール

- フォークして新しいブランチを作成してください
- 変更は小さく、具体的にしてください
- 変更内容には日本語（または英語）の説明を付けてください

## プルリクエスト

1. フォークを作成
2. `main` ブランチを最新に保つ
3. 新規ブランチを作成
4. 変更をコミット
5. プルリクエストを送信

## テスト

現在は単体テストが `tests/test_main.py` にあります。変更後はテストを追加し、実行してください。

```powershell
git checkout main
git pull
python -m pip install -e .
python -m pytest
```
