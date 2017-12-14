FROM python:3

RUN mkdir -p /usr/src/spray/extract_output
WORKDIR /usr/src/spray

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./sprayExtract.py" ]