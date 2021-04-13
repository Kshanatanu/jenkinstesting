FROM python:3.8.5-apline
RUN pip install -upgrade pip
COPY ./requirments.txt .
RUN pip install -r requirments.txt
COPY ./tokenpro /app
WORKDIR /app
COPY ./entrypoint.sh/
ENTRYPOINT ["sh","entrypoint.sh"]
	
