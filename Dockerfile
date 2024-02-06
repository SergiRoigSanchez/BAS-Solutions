FROM python

WORKDIR /app
COPY . /app

RUN pip3 install shodan
RUN mkdir /root/.shodan

EXPOSE 3000

CMD [ "/bin/python3", "./tasca1_shodan.py" ]
