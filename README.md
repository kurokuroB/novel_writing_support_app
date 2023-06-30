# novel_writing_support_app

## 概要

簡易的な執筆支援アプリ

## エンドポイント

- チャット用  
  https://novel-writing-support-app-hzmhfp5tya-uc.a.run.app/chat

  - コマンド  
    `curl -X POST -d "model=gpt-3.5-turbo-16k&text=10000字程度の短編評価も可能" https://novel-writing-support-app-hzmhfp5tya-uc.a.run.app/chat`

- 新規性確認用（beta）  
  https://novel-writing-support-app-hzmhfp5tya-uc.a.run.app/check_novelty

  - コマンド

    `curl -X POST -d "text=あらすじ" https://novel-writing-support-app-hzmhfp5tya-uc.a.run.app/check_novelty`
