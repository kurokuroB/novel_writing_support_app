from flask import Flask, request
import openai

app = Flask(__name__)
# app.config["JSON_AS_ASCII"] = False  # json出力時の、文字化けを防止


# ルーティング


# シンプルな小説採点
@app.route("/evaluation", methods=["POST"])
def evaluation():
    """本文の講評を行う"""
    # 定数

    model = request.form.get("model", "gpt-3.5-turbo-16k")  # 特に指定なければ16k使う
    script = request.form.get("text", "")

    answer = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": script},
        ],
    )

    evaluation = answer["choices"][0]["message"]["content"]

    return evaluation


# おまじない
if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")  # host='0.0.0.0'で外部公開を行う
