FROM python:3.10-slim-bullseye

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100

ENV PORT=80

# -----------------------------------------------

EXPOSE 80:80

WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
COPY . .

CMD streamlit run 🏠_Home_Page.py \
    --server.headless true \
    # --server.enableCORS false \
    --browser.gatherUsageStats false \
    # --server.enableXsrfProtection false \
    --browser.serverAddress="0.0.0.0" \
    --server.port 80
