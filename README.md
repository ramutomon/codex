# ChatGPT Pro 無料 Open Source Codex OSS

このリポジトリは、ChatGPT Pro 体験を補完する Open Source Codex OSS 向けの Python プロジェクトです。

## 概要

- `codex` パッケージは、Open Source で使いやすい Python 実行環境を提供します。
- ChatGPT Pro などの AI 活用に向けた開発のベースとして利用できます。
- GitHub で公開し、OSS としてコミュニティ貢献を受け入れます。

## セットアップ

```powershell
cd C:\Users\user\Documents\codex
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e .
```

## 実行

```powershell
.\.venv\Scripts\Activate.ps1
python -m codex
```

## 開発

- `src/` - Python ソースコード
- `tests/` - 単体テスト
- `pyproject.toml` - パッケージ設定
- `LICENSE` - ライセンス情報

## 貢献

1. フォークを作成
2. ブランチを切る
3. 変更をコミット
4. プルリクエストを提出

詳細は `CONTRIBUTING.md` を参照してください。

## ライセンス

このプロジェクトは `MIT License` の下で公開されています。
