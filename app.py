from flask import Flask, request
import openai

app = Flask(__name__)
# app.config["JSON_AS_ASCII"] = False  # json出力時の、文字化けを防止


# ルーティング


@app.route("/chat", methods=["POST"])
def chat():
    """chatgptとのchatを行う。"""

    model = request.form.get("model", "gpt-3.5-turbo-16k")  # 特に指定なければ16k使う
    text = request.form.get("text", "")

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
        ],
    )

    content = response["choices"][0]["message"]["content"]

    return content


# おまじない
if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")  # host='0.0.0.0'で外部公開を行う
