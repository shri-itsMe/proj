# syntax=docker/dockerfile:1
FROM python
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
EXPOSE 8000
COPY . .
# ENV PYTHONPATH="/app/src:$PYTHONPATH"
CMD ["uvicorn", "hello_api.routes:app", "--host", "0.0.0.0", "--port", "2005"]
# CMD ["ls", "-la", "/app/src/hello_api/"]