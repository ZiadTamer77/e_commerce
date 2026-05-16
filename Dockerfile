FROM python:3.13 AS build-stage


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

RUN pip install --upgrade pip && pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY docker-entrypoint.sh wait-for-it.sh ./
RUN chmod +x ./docker-entrypoint.sh ./wait-for-it.sh

FROM python:alpine3.23 AS runtime-stage


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

COPY --from=build-stage --chown=appuser:appgroup /app /app
COPY --from=build-stage --chown=appuser:appgroup /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=build-stage --chown=appuser:appgroup /usr/local/bin /usr/local/bin


USER appuser

EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]