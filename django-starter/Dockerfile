FROM python:3.11
WORKDIR /app
RUN apt-get update && apt-get install -y netcat-traditional
COPY . .
RUN mkdir /logs 
EXPOSE 8000

RUN pip install -r /app/requirements.txt
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
