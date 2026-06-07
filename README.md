# Codex Project

PythonベースのCodexプロジェクト環境です。

## セットアップ

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt
```

## ファイル構成

- `src/` - Pythonソース
- `tests/` - テスト
- `pyproject.toml` - プロジェクト設定

## 実行

```powershell
.\.venv\Scripts\Activate.ps1
python -m codex
```
