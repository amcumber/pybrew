FROM python:3.9-slim AS base
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base as runtime

# Copy virtual env
COPY --from=base /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# create ans switch to a new user

RUN useradd --create-home brewuser
WORKDIR /home/brewuser
USER brewuser

# Install application into container
COPY . .
