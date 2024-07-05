FROM python:3-slim

WORKDIR /usr/src/app

RUN apt update -y \
    && apt install -y --no-install-recommends \    
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]
CMD [ "app" ]