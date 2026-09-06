import os
import json
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルの中身を読み込む
load_dotenv()

# Geminiの準備（.envのAPIキーを読み込む）
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

class EssayRequest(BaseModel):
    topic: str
    essay: str

@app.get("/")
def home():
    return FileResponse("templates/writing.html")

@app.post("/submit")
def submit(request: EssayRequest):
    print("AI(Gemini)に添削を依頼中...")
    
    # AIへの指示（システムプロンプト）
    system_instruction = """
    あなたは優秀な英語教師です。ユーザーのトピックと英作文を評価し、必ずJSON形式で出力してください。
    出力するJSONのキーは以下の通りにしてください。
    - overall_score: 100点満点のスコア (数値)
    - feedback_summary: 全体的なフィードバック (文字列)
    - mistakes: 以下のキーを持つオブジェクトの配列
      - original: 元の誤った文章
      - corrected: 修正後の文章
      - category_tag: "Grammar", "Vocabulary", "Spelling", "Unnatural" のいずれか
      - feature: 誤りの具体的な理由
    """
    
    # モデルの設定（安くて速い gemini-1.5-flash を使用し、JSON出力モードをONにする）
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction,
        generation_config={"response_mime_type": "application/json"}
    )
    
    # ユーザーからの入力
    user_prompt = f"トピック: {request.topic}\nエッセイ: {request.essay}"
    
    # Gemini APIを呼び出す
    response = model.generate_content(user_prompt)
    
    # 返ってきたJSONの文字列を、Pythonのデータに変換
    ai_result_str = response.text
    result_data = json.loads(ai_result_str)
    
    print("添削完了！画面に返却します。")
    
    # 画面側（JavaScript）へ返す
    return result_data