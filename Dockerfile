FROM python:3.9-buster

WORKDIR /
ADD . /

# https://timesaving.hatenablog.com/entry/2022/10/03/150000

ENV POETRY_HOME="/opt/poetry" \
    # 以下設定で、コンテナ上に直接パッケージをインストールするようにする。
    POETRY_VIRTUALENVS_CREATE=false 

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get clean
RUN curl -sSL https://install.python-poetry.org/ | python -

#package install
COPY pyproject.toml poetry.lock /
RUN poetry install --only main

ENTRYPOINT ["python", "app.py"]