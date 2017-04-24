FROM python

MAINTAINER Rodolfo Ferrazzi Carrara <rfcarrara@gmail.com>

ADD . /bot

WORKDIR /bot

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["example.py"]