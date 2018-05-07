FROM python:3.6

ADD . /spider

WORKDIR /spider

RUN pip install -r requirements.txt

ENTRYPOINT ["scrapy", "crawl", "get_offers", "-o", "offers.json"]
