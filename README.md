# english-writing-feedback

## Motivation
 I study English for the IELTS and the Eiken (Japanese English Proficiency Test).
Writing is one of the most challenging skills for many non-native English learners.

When I practice writing, I often use ChatGPT and other large language models (LLMs) to receive feedback.
However, simply receiving corrected sentences does not always lead to long-term improvement.
Many learners understand the corrections at the moment, but they often fail to retain them or apply them in future writing.

This project aims to help learners internalize their mistakes by providing opportunities for repeated practice.
 
## プロジェクト動機
IELTSや英検のために英語を習慣的に勉強している。ライティングセクションの強化はノンネイティブにとって難しいセクションの一つである。
　ライティングを練習する時、英作文添削のためにChatGPTのような生成AIを用いる。彼らは非常に的確な添削を行う。一方で学習者が添削内容を理解できたからと言って、それが知識として定着し次のライティングで適切に使えるかは別問題である。
　このプロジェクトでは、ライティングにおける添削内容の定着に焦点を当てる。AIによる添削を元に、繰り返し間違えた内容を復習できるようなシステムを構築する。


## Overview
This project is an AI-powered English writing learning support system.

The system first analyzes and corrects a learner's English writing using AI. It then categorizes and scores the learner's mistakes based on their types and frequency. Based on the results, the system generates personalized practice exercises that target the learner's weaknesses.

By combining AI feedback with adaptive practice, the project aims to help learners not only understand their mistakes but also retain and apply what they have learned in future writing.

## 概要

本プロジェクトは、英語学習者向けのAI英作文添削システムである。

従来の添削ツールは誤りを修正することに重点を置いているが、本システムでは添削内容の定着を支援することを目的とする。AIによる添削結果をもとに、学習者が誤りを繰り返し学習できる仕組みを提供し、知識の定着とライティング能力の向上を支援する。

## System Architecture

The system consists of the following workflow:

1. **AI Feedback**

   * The learner submits an English essay.
   * An LLM analyzes the essay and returns corrections and explanations in JSON format.

2. **Feature Extraction**

   * The JSON output is parsed to extract error features, such as articles, tense, prepositions, word choice, and sentence structure.

3. **Scoring**

   * The extracted features are converted into category-based scores to identify the learner's strengths and weaknesses.

4. **Personalized Practice Generation**

   * Based on the scores, the system generates personalized practice questions using an LLM.
   * The generated exercises focus on the learner's weakest areas to reinforce long-term retention.

## システム構成

本システムは、以下の流れで学習者を支援する。

1. **AIによる英作文添削**

   * 学習者が英作文を入力する。
   * LLMが英作文を添削し、修正内容や解説をJSON形式で出力する。

2. **特徴量抽出**

   * JSONデータから、冠詞・時制・前置詞・語彙・文構造などの誤りを抽出する。

3. **スコアリング**

   * 抽出した特徴量をもとに、各項目の理解度や習熟度をスコアとして算出する。

4. **個別最適化された問題生成**

   * スコアに基づいて、LLMが学習者の弱点に応じた練習問題を生成する。
   * 学習者は反復学習を通じて、添削内容の定着を目指す。


## Development Roadmap

* [ ] Design the JSON schema

  * Design a structured format for AI feedback.

* [ ] Build the feedback acquisition system

  * Develop a system that retrieves essay feedback from an LLM API in JSON format.

* [ ] Collect feedback data

  * Build a dataset for analysis and evaluation.

* [ ] Feature extraction

  * Extract error features such as articles, tense, prepositions, vocabulary, and sentence structure.

* [ ] Develop a scoring method

  * Design and implement a scoring algorithm to quantify learners' strengths and weaknesses.

* [ ] Generate personalized practice exercises

  * Generate practice questions based on each learner's scores using an LLM.

* [ ] Evaluate and improve the system

  * Assess the effectiveness of the system and refine the scoring and question generation methods.


## 今後の開発計画

* [ ] JSONレスポンス設計

  * 添削結果を構造化データとして取得できる形式を設計する。

* [ ] 添削データ取得システムの構築

  * LLM APIを利用し、英作文の添削結果をJSON形式で取得する。

* [ ] データ収集

  * 添削データを蓄積し、分析可能なデータセットを構築する。

* [ ] 特徴量分析

  * 添削データから誤りの種類（冠詞・時制・前置詞・語彙など）を抽出し、特徴量として整理する。

* [ ] スコアリング手法の開発

  * 特徴量をもとに学習者の弱点を定量化するアルゴリズムを設計・実装する。

* [ ] 個別最適化問題生成

  * スコアに応じてLLMが学習者ごとの練習問題を生成する。

* [ ] 学習履歴の活用

  * 学習履歴を蓄積し、スコアの推移や成長を可視化する。


## Other Features

### Writing Modes

* Academic
* General
* Business

### CEFR-Based Learning

* Support for CEFR levels (A1–C2)
* Level-appropriate practice exercises
* Adaptive feedback based on proficiency

### AI-Powered Learning

* AI-powered essay correction
* Error analysis and scoring
* Personalized practice generation
* Learning progress tracking


## その他の機能 

### ライティングモード 

* **Academic**：IELTS・英検などのアカデミックライティング
* **General**：日常的な英語表現や一般的なライティング
* **Business**：ビジネスメールや報告書などの実務向けライティング

### CEFRレベル別学習 

* CEFR（A1–C2）に対応
* レベルに応じた練習問題の提供
* 習熟度に応じた適応的なフィードバック

### AI学習支援 

* AIによる英作文添削
* 誤りの分析・スコアリング
* 個別最適化された練習問題の生成
* 学習履歴・成長の可視化
