# ETHICA VTuber Studio コーポレートサイト

黒川さんの会社 Ethica 名義の VTuber 支援スタジオのサイト。静的 HTML/CSS/JS（フレームワーク・ビルド不要）。

- **デザイン・実装: GPT-6 astra（codex exec）**。パック（design_direction.md / facts.md / 参考画像 / 事業計画スライド）は `~/codex_isolated_runs/2026-10-29_ethica_site/`。制作メモは `DESIGN_NOTES_gpt.md`
- デザイン参考: https://miraimusubi.jp （暗いファーストビュー・紙色のセクション・英字見出し・青→紫の Contact 帯）
- 事業構成参考: https://samurai-partners.jp の 4 事業を VTuber 版に置き換え
  - 01 ENTERTAINMENT（VTuber 活動サポート／VTuber イベント／自社 IP 番組／イベント企画・運営）
  - 02 MARKETING（VTuber タイアップ／コンテンツプロデュース／SNS／グッズ・D2C）
  - 03 CREATIVE（キャラクター制作／映像／デザイン／ブランディング・構成）
  - 04 CREATOR SUPPORT（税務／法務・契約／資金・機材の計画／条件の事前開示）← サムライの「ファイナンス事業」の VTuber 版
- 訴求文・支援項目・対象 A/B/C・料金条件の表は 2026-09-08 のデザイン提案（支援事務所版）と有識者ご意見用スライドに揃えている
- ヒーローのキャラクター画像は **GPT 画像生成（gpt-image-2）による仮ビジュアル**。原画 PNG と生成プロンプト、Midjourney 用プロンプトは `../site_assets_素材/`。Midjourney で作り直したら `assets/img/hero_wide.{jpg,webp}`（16:9）と `hero_portrait.{jpg,webp}`（2:3）を同名で上書きすれば HTML の変更は不要
- Claude が先に組んだ第 1 版は `../site_design_サイトデザイン/2026-10-29_claude_v1/` に保管（黒田レビュー済み・不採用）

## ファイル構成

| パス | 内容 |
|---|---|
| `index.html` | トップ（ヒーロー → Service 4 事業 → Message/MVV → Company → Access → Contact） |
| `entertainment.html` `marketing.html` `creative.html` `support.html` | 事業ページ（サービス 01〜04・相談 CTA・他事業導線。entertainment に対象 A/B/C と流れ、support に料金・条件表） |
| `privacy.html` | プライバシーポリシー |
| `assets/style.css` | 共通スタイル（末尾にスマホ用ヒーローの上書きを Claude が追記） |
| `assets/main.js` | ヘッダー切替・モバイルメニュー・スクロール表示（JS 無効でも内容は表示される） |
| `assets/img/` | ヒーロー画像（jpg + webp） |

## 更新手順

1. HTML / CSS を直接編集（共通ヘッダー・フッターは各ページに同じものが入っている。変えるときは 6 ページとも）
2. `git add -A && git commit && git push`（GitHub Pages が自動で反映。数十秒〜数分）
3. 公開前にデザイン監修（黒田 = `design-reviewer` エージェント）を通す

## 公開

- GitHub: https://github.com/Tsubasa-hub/ethica-vtuber-studio （public。GitHub Pages は public リポジトリが必要）
- URL: https://tsubasa-hub.github.io/ethica-vtuber-studio/
- 全ページ `<meta name="robots" content="noindex,nofollow">` を付けている。本公開時に 6 ページから削除する
- 独自ドメイン・Vercel への移行はこのリポジトリをそのまま Import すればよい（静的サイトなので設定不要）

## 未確定（確定後に差し替え）

- 設立・代表者・所在地（Company / Access）
- 問い合わせ先（メールアドレス・X アカウント）。確定したら Contact の「相談窓口は準備中です」をボタン（mailto / X のリンク）に差し替える
- プライバシーポリシーの制定日
- キャラクター画像（仮）。事業ページの SVG 線画も写真・イラストに差し替え可
- 「税理士・弁護士と連携」「解約後の活動制限なし」は訴求として掲載している。黒川さんが実現できるか確認が必要
