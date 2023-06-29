from flask import Flask, request
import openai
from gensim.models.doc2vec import Doc2Vec
from janome.tokenizer import Tokenizer
import numpy as np


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # json出力時の、文字化けを防止

doc2vec = Doc2Vec.load("./model/doc2vec")
tokenizer = Tokenizer()

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


# アイデアの新規性を確認（beta)
@app.route("/check_novelty", methods=["POST"])
def check_novelty():
    text = request.form.get("text", "")
    wakati = list(tokenizer.tokenize(text, wakati=True))
    wakati_vector = doc2vec.infer_vector(wakati)

    # https://radimrehurek.com/gensim/models/keyedvectors.html
    # 10個の類似小説を取り出す
    most_similars = doc2vec.docvecs.most_similar(wakati_vector, topn=10)

    similaritys = []
    for idx, similarity in most_similars:
        similaritys.append(similarity)
    mean_similarity = np.mean(similaritys)

    return f"過去作類似度:{mean_similarity}"


# おまじない
if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")  # host='0.0.0.0'で外部公開を行う
