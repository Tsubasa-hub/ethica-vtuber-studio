# ETHICA VTuber Studio コーポレートサイト

黒川さんの会社 Ethica 名義の VTuber 支援スタジオのサイト。静的 HTML（フレームワーク不使用・ビルド不要）。

- デザイン参考: https://miraimusubi.jp （配色・英字見出し・暗いヒーロー・青→紫の Contact 帯）
- 事業構成参考: https://samurai-partners.jp の 4 事業を VTuber 版に置き換え
  - 01 ENTERTAINMENT（VTuber 活動サポート／VTuber イベント／自社 IP 番組／イベント企画・運営）
  - 02 MARKETING（VTuber タイアップ／コンテンツプロデュース／SNS／グッズ・D2C）
  - 03 CREATIVE（キャラクター制作／映像／デザイン／ブランディング・構成）
  - 04 CREATOR SUPPORT（税務／法務・契約／資金・機材の計画／条件の事前開示）← サムライの「ファイナンス事業」の VTuber 版
- 訴求文・支援項目・対象 A/B/C・料金条件の表は 2026-09-08 のデザイン提案（支援事務所版）と同じ内容

## ファイル構成

| パス | 内容 |
|---|---|
| `src/*.html` | 各ページの本文（編集はこちら） |
| `build.py` | `src/` に共通ヘッダー・フッター・`<head>` を付けてルートに書き出す |
| `index.html` ほか | 生成物（直接編集しない） |
| `assets/style.css` | 全ページ共通スタイル |
| `assets/main.js` | ヘッダー切替・モバイルメニュー・スクロール表示 |

## 更新手順

1. `src/` の該当ファイルを編集（共通部分は `build.py` 内の HEAD / header() / FOOTER）
2. `python3 build.py`
3. `git add -A && git commit && git push`（GitHub Pages が自動で反映。数十秒〜数分）

## 公開

- GitHub: https://github.com/Tsubasa-hub/ethica-vtuber-studio （public。GitHub Pages は public リポジトリが必要なため）
- URL: https://tsubasa-hub.github.io/ethica-vtuber-studio/
- 全ページ `noindex` を付けている。本公開時に `build.py` の `<meta name="robots">` 行を削除する
- 独自ドメイン・Vercel への移行はリポジトリをそのまま Import すればよい（静的サイトなので設定不要）

## 未確定（確定後に差し替え）

- 設立・代表者・所在地（Company / Access）
- 問い合わせメールアドレス（`contact@ethica.example` は仮）と X のDM リンク（`#`）
- プライバシーポリシーの制定日
- 画像素材（現在は CSS の抽象グラフィック）
- 「税理士・弁護士と連携」「解約後の活動制限なし」は訴求として掲載している。黒川さんが実現できるか確認が必要
