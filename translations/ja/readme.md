# ホーム

**パッシブ・フォールトトレランス。ガラスボックスAI。1つの数学的補正。**

> QWAV は、 [QNFO](https://github.com/QNFO/.github)の旗艦研究イニシアチブです。これは、 **すべての人の集合的利益のために**知識を前進させる科学研究インキュベーターです。QNFO は Empowering Change（501c3）の研究上のアイデンティティです。すべての作業は、 [QNFO コンテンツ・ライセンス契約](https://github.com/QNFO/gitbook/blob/main/LICENSE/README.md) および [行動規範](https://github.com/QNFO/gitbook/blob/main/CODE_OF_CONDUCT.md).

***

## QWAV とは

QWAV は、量子コンピューティングと人工知能のために、アルキメデス的（連続的）幾何を超距離的（木ベースの）幾何へ置き換えます。Bruhat-Tits 木 — p進数論に由来する構造 — は、強三角不等式によってパッシブな誤り抑制を提供し、4K で動作し、能動的な誤り訂正を必要としません。

## 主な結果

* **深さ7で論理誤りゼロ** — 三値 Bruhat-Tits 木エンコーディング、物理誤り率40%までで検証済み
* **階層的な誤り封じ込め** — 誤りは各木の枝の内部にのみ伝播し、枝をまたぐことはありません
* **ガラスボックスAI** — その構造自体により意思決定が監査可能な、木トポロジー上のニューラルアーキテクチャ
* **40原子の中性原子仕様** — 実証済みの実験能力の範囲内

## インタラクティブ・デモ

| #  | アーティファクト        | ライブデモ                                                       | 説明                              |
| -- | --------------- | ----------------------------------------------------------- | ------------------------------- |
| A1 | 誤り封じ込め          | [デモ](https://qnfo.github.io/ultrametric-error-confinement/) | Bruhat-Tits 木の誤りシミュレーション        |
| A2 | Q-PNA プレイグラウンド  | [デモ](https://qnfo.github.io/Q-PNA/)                         | 量子ネイティブ p進ニューラルアーキテクチャ・エクスプローラー |
| A3 | 収束エクスプローラー      | [デモ](https://qnfo.github.io/ultrametric-convergence/)       | 超距離クラスタリングとユークリッドクラスタリングの比較     |
| A4 | 木距離             | [デモ](https://qnfo.github.io/tree-distance/)                 | インタラクティブな共分散距離の比較               |
| A5 | ハードウェア・ビジュアライザー | [デモ](https://qnfo.github.io/hardware-pathway/)              | 3D 中性原子木の可視化                    |
| K1 | 技術ハブ            | [ハブ](https://qnfo.github.io/QWAV/)                          | ライブデモ付きのプログラム概要                 |

## プログラム管理（すべて公開）

| 機能           | リンク                                                                        |
| ------------ | -------------------------------------------------------------------------- |
| **Wiki**     | [6ページ — アーキテクチャ、モジュール、出版物](https://github.com/QNFO/QWAV/wiki)              |
| **ディスカッション** | [セッション記録、スプリント報告](https://github.com/QNFO/QWAV/discussions)                |
| **カンバンボード**  | [11件の課題 — 優先度、スプリント、ステータス](https://github.com/orgs/QNFO/projects/1)        |
| **課題**       | [公開3件、クローズ22件](https://github.com/QNFO/QWAV/issues)                        |
| **リリース**     | [v2.73 — スプリント19-21](https://github.com/QNFO/QWAV/releases)                |
| **マイルストーン**  | [S19（クローズ）、S20（クローズ）、S21（公開）](https://github.com/QNFO/QWAV/milestones)     |
| **ラベル**      | [19 — P0-P3、blocked、research、testing](https://github.com/QNFO/QWAV/labels) |

## ドキュメント

| 文書                                                                                         | 目的                             |
| ------------------------------------------------------------------------------------------ | ------------------------------ |
| [PROJECT STATE.md](https://github.com/QNFO/gitbook/blob/main/PROJECT%20STATE.md)           | LLM 引き継ぎ用の現在のプログラム状態           |
| [CHANGELOG.md](https://github.com/QNFO/gitbook/blob/main/CHANGELOG.md)                     | 時系列の変更ログ（v2.74）                |
| [CHARTER.md](https://github.com/QNFO/gitbook/blob/main/CHARTER.md)                         | プログラムの範囲、制約                    |
| [LEARNINGS.md](https://github.com/QNFO/gitbook/blob/main/LEARNINGS.md)                     | 29の教訓、うち1件は BLOCKING           |
| [BRAND-STRATEGY.md](https://github.com/QNFO/gitbook/blob/main/briefings/BRAND-STRATEGY.md) | QNFO/QWAV/Rowan のブランド・アイデンティティ |
| [既存業績カタログ](https://github.com/QNFO/gitbook/blob/main/briefings/prior-work-catalog.md)      | 30件の外部出版物、7カテゴリ                |

## テストスイート

* **102件のテスト**：42件の構造テスト（unittest）＋60件のパラメータ化テスト（pytest）
* CDPコンソールキャプチャ付きのブラウザ・スモークテスト
* 102/102 件すべて合格

## 出版物

Zenodo 上のオープンアクセス出版物40件以上。 [完全なカタログ](https://qnfo.github.io/ultrametric-tree-universality/pub-hub.html)をご覧ください。主な出版物：

* [超距離量子コンピューティングの基礎](https://doi.org/10.5281/zenodo.15107688)
* [超距離誤り封じ込めの検証](https://doi.org/10.5281/zenodo.15113616)
* [超距離誤り封じ込めの対称拡張](https://doi.org/10.5281/zenodo.15129661)
* [木は実在する](https://doi.org/10.5281/zenodo.15241485)
* [すべての底にある木](https://doi.org/10.5281/zenodo.15276773)

## ライセンス

**QNFO コンテンツ・ライセンス契約 v1.1** — 詳細は [LICENSE](https://github.com/QNFO/gitbook/blob/main/LICENSE/README.md) をご覧ください。

非商用利用のみ。帰属表示が必要です。特許先行技術の引用は必須です。すべての QNFO 組織および rwnq8 個人リポジトリにはこのライセンスが適用されます。2026-05-24 時点で、すべてのリポジトリに遡及的に有効です。

_主要条件：_ 非独占、譲渡不可、取消可能。商用利用には別途契約が必要です。無許可の商用利用には85%の違約金。準拠法はスイス法、仲裁はジュネーブのICC。

***

_QNFO — QWAV のオープンソースの拠点。公開物はすべて公開。追跡対象はすべて追跡。_

***

## 翻訳

このドキュメントは GitBook AI 翻訳により 10以上の言語で利用できます。上部ナビゲーションバーの言語セレクターを使って言語を切り替えてください。

