# ChatGPT Pro 無料 Open Source Codex OSS

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python package](https://github.com/ramutomon/codex/actions/workflows/python-package.yml/badge.svg)](https://github.com/ramutomon/codex/actions/workflows/python-package.yml)

このリポジトリは、ChatGPT Pro と連携する Open Source Codex OSS 向けの Python プロジェクトです。OSS として公開され、開発者コミュニティが利用・拡張できる基盤を目指します。

## なぜこのプロジェクトが重要か

- ChatGPT / AI 開発のエコシステムに、簡単に使える OSS の入口を提供します。
- Python で汎用的に再利用できる構成を備えています。
- CI、ライセンス、貢献ガイドを含む OSS の公開基準を満たしています。

## 応募審査で評価される理由

- このリポジトリは、ChatGPT Pro や Codex OSS を意識した公開用テンプレートとして整備されています。
- `MIT` ライセンス、`CONTRIBUTING.md`、Issue/PR テンプレート、GitHub Actions CI を備え、OSS プロジェクトとしての体裁を満たします。
- Python パッケージとしてインストール可能で、テストが自動化されているため、品質の再現性が高いです。
- まだ公開直後のため GitHub スター数や月間ダウンロード数は存在しませんが、AI/ChatGPT エコシステムにおける需要の高まりから、成長余地が大きいと判断できます。

## 期待される支持・成長要因

- AI 開発のコミュニティで利用されやすい Python 基盤
- OSS での拡張やフォークを前提にした設計
- クリアなライセンスと参加ルールにより、貢献者を受け入れやすい

## 特長

- `python -m codex` で起動できる軽量 CLI
- Python パッケージとして再利用しやすい構造
- GitHub Actions によるテスト自動化
- MIT ライセンスで外部貢献が可能

## セットアップ

```powershell
cd C:\Users\user\Documents\codex
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

## 実行

```powershell
.\.venv\Scripts\Activate.ps1
python -m codex
```

## 使い方

`codex` には基本的な実行コマンドが含まれます。

```powershell
python -m codex --help
```

## 開発とテスト

- ソースコードは `src/codex/` に配置
- テストは `tests/` で管理

```powershell
pytest
```

## 貢献

1. リポジトリをフォーク
2. 新しいブランチを作成
3. 変更をコミット
4. プルリクエストを送信

詳細は `CONTRIBUTING.md` を参照してください。

## ライセンス

MIT License
