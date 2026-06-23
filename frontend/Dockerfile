FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --index-url https://pypi.org/simple --trusted-host pypi.org -r requirements.txt

COPY streamlit_app.py .

CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]