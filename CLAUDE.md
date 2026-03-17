# CLAUDE.md — ari-coach プロジェクト作業手順書

このファイルはClaude Code（クロコ）がari-coachリポジトリで作業する際に参照する指示書です。

---

## プロジェクト概要

ari-coachは、在り（Ari）3.0のセルフコーチングシステムです。
コーチングプロンプト（最強セルフコーチング_プロンプト_3.0.md）を中心に、
Streamlitアプリ（app.py）として動作します。

---

## リポジトリ構成

```
ari-coach/
├── CLAUDE.md                          # この手順書（クロコ用）
├── README.md                          # プロジェクト説明
├── app.py                             # Streamlitアプリ本体
├── requirements.txt                   # Pythonパッケージ
├── runtime.txt                        # Pythonバージョン指定
├── .env.example                       # 環境変数のサンプル
├── .gitignore                         # Git除外設定
├── 最強セルフコーチング_プロンプト_3.0.md  # コーチングプロンプト本体
└── data/sessions/                     # セッションデータ保存先
```

---

## GitHubへのファイルアップ手順

### 基本的な流れ

```bash
# 1. リポジトリのクローン（初回のみ）
git clone https://github.com/katsuhikoarie-coach/ari-coach.git
cd ari-coach

# 2. 最新の状態に更新
git pull origin main

# 3. ファイルを編集・追加する

# 4. 変更内容を確認
git status
git diff

# 5. ステージングに追加
git add ファイル名
# 全ファイルを追加する場合
git add .

# 6. コミット（日本語でOK）
git commit -m "変更内容の説明"

# 7. プッシュ
git push origin main
```

### コミットメッセージのルール

変更内容が一目でわかるように書く。

```
# 例
git commit -m "feat: Phase 6の行動コミットメントフローを4ステップに改良"
git commit -m "fix: 危機介入プロトコルに希死念慮対応と相談窓口を追加"
git commit -m "remove: クライアント固定プロファイルを削除（セルフコーチング用に変更）"
git commit -m "add: CLAUDE.md を追加"
```

---

## コーチングプロンプトの更新手順

プロンプト（最強セルフコーチング_プロンプト_3.0.md）を変更した場合：

```bash
# 変更後にアップする
git add 最強セルフコーチング_プロンプト_3.0.md
git commit -m "update: プロンプト ○○を改良"
git push origin main
```

---

## Streamlitアプリの更新手順

app.py を変更した場合：

```bash
git add app.py
git commit -m "fix: ○○の不具合を修正"
git push origin main
```

---

## 注意事項

- `.env` ファイルは絶対にコミットしない（APIキーが含まれるため）
- `.gitignore` に `.env` が含まれていることを毎回確認する
- `data/sessions/` 内のセッションデータも基本的にはコミットしない
- 大きな変更をする前は必ず `git pull` で最新状態にする

---

## よく使うコマンド一覧

| やりたいこと | コマンド |
|------------|---------|
| 現在の状態確認 | `git status` |
| 変更差分を見る | `git diff` |
| 変更履歴を見る | `git log --oneline` |
| 特定のファイルだけ戻す | `git checkout -- ファイル名` |
| 直前のコミットを修正 | `git commit --amend` |
| ブランチ一覧 | `git branch` |

---

*このファイルはクロコ（Claude Code）への作業指示書です。*
*更新日：2026年3月*
