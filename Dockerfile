FROM python:3.10-22.04_stable

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y gcc-13 \
    g++-13 git graphviz cmake\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv && pipenv install --skip-lock
RUN pipenv run freshquark

WORKDIR /app/quark
ENTRYPOINT ["pipenv", "run"]
