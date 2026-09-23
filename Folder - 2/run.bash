#!/usr/bin/env bash
# ==============================================================================
# Capstone Assignment 2: Folder - 2 Launcher Script
# Candidate: Souvik Nandi (Student ID: 12023002028046)
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CAPSTONE_DIR="$SCRIPT_DIR/Capstone Assignment - 2"

if [ -f "$CAPSTONE_DIR/run.bash" ]; then
    exec "$CAPSTONE_DIR/run.bash" "$@"
else
    echo "[ERROR] Could not find Capstone Assignment runner at: $CAPSTONE_DIR/run.bash"
    exit 1
fi
