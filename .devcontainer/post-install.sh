#!/bin/bash
poetry install;

# Get the Poetry virtual environment path
VENV_PATH=$(poetry env info --path 2>/dev/null)

if [ -z "$VENV_PATH" ]; then
  echo "No Poetry environment found. Did you run 'poetry install'?"
  exit 1
fi

# Ensure VS Code settings directory exists
SETTINGS_DIR="/home/vscode/.vscode-server/data/Machine"
SETTINGS_FILE="$SETTINGS_DIR/settings.json"

mkdir -p "$SETTINGS_DIR"

# If settings.json doesn't exist, create a default one
if [ ! -f "$SETTINGS_FILE" ]; then
  echo "{}" > "$SETTINGS_FILE"
fi

# Update VS Code settings to use the Poetry virtual environment
jq --arg venv "$VENV_PATH/bin/python" '.["python.defaultInterpreterPath"] = $venv' \
  "$SETTINGS_FILE" > "$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"

echo "✅ Updated VS Code to use Poetry environment: $VENV_PATH"
