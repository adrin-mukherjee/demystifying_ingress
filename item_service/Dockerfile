FROM python:3.10-slim AS build
WORKDIR /code
COPY . /code/

FROM python:3.10-slim
WORKDIR /code
COPY --from=build /code /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 9091
CMD ["python3", "main.py"]

