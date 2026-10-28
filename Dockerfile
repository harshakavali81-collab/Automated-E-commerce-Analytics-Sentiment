FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --uid 10001 --create-home --shell /usr/sbin/nologin commerce && \
    mkdir -p /app/data/raw /app/data/interim /app/data/processed /app/reports && \
    chown -R commerce:commerce /app/data /app/reports
USER commerce
EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=6s --start-period=60s --retries=3 CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8501/_stcore/health',timeout=5)" || exit 1
CMD ["sh","-c","python -m scripts.refresh --demo && exec streamlit run dashboard/app.py --server.address=0.0.0.0 --server.port=8501 --server.headless=true"]
