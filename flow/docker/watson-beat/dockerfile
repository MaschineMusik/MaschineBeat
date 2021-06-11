FROM python:2.7

WORKDIR /usr/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD [ "python", "./wbDev.py" ]


