FROM library/python:3.12-bullseye

ARG USER=vscode
ARG DEBIAN_FRONTEND=noninteractive

# Install system dependencies in a single layer
RUN apt update && apt install -y --no-install-recommends \
    sudo jq vim \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Create the user and grant sudo privileges
RUN useradd -m -s /usr/bin/bash ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER} \
    && chmod 0440 /etc/sudoers.d/${USER}

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set the working directory
WORKDIR /workspaces/survey-extractor