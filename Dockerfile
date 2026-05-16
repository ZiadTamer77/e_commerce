FROM python:3.13-slim-trixie AS build-stage

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser \
  && chown -R appuser:appgroup /app/

# Build deps for mysqlclient
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  gcc \
  pkg-config \
  default-libmysqlclient-dev \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY docker-entrypoint.sh wait-for-it.sh ./
RUN chmod +x ./docker-entrypoint.sh ./wait-for-it.sh

COPY . .

FROM python:3.13-slim-trixie AS runtime-stage

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Runtime lib only — no gcc
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  default-libmysqlclient-dev \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser \
  && chown -R appuser:appgroup /app/
COPY --from=build-stage --chown=appuser:appgroup /app /app
COPY --from=build-stage /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=build-stage /usr/local/bin /usr/local/bin

USER appuser
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]