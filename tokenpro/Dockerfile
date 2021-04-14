FROM python:3.8.9-alpine
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./tokenpro /app
WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh","entrypoint.sh"]
	
