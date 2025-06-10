FROM python:3.9

WORKDIR /app

COPY . .

# Install numpy first to make sure it's available before others
RUN pip install numpy==1.23.5

# Now install everything else
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

