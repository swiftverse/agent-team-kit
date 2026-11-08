#!/usr/bin/env bash
# Runs every brief in inbox/ through the team, one at a time.
# Agents get no shell in this mode, so they can't push, deploy or delete.
# Usage: BUDGET_PER_BRIEF=5 ./scripts/overnight.sh
set -uo pipefail
cd "$(dirname "$0")/.."

BUDGET="${BUDGET_PER_BRIEF:-5}"
TOOLS="Agent,Read,Write,Edit,Glob,Grep,WebSearch,WebFetch"
mkdir -p inbox/done runs
touch runs/MORNING.md

for brief in inbox/*.md; do
  [ -e "$brief" ] || { echo "No briefs in inbox/."; break; }
  name="$(basename "$brief" .md)"
  id="$(date +%Y%m%d-%H%M%S)-$name"
  run="runs/$id"
  mkdir -p "$run"
  cp "$brief" "$run/brief.md"

  echo "Running $name (limit \$$BUDGET)"
  claude -p "/team $run/brief.md" \
    --tools "$TOOLS" \
    --allowedTools Agent Read Write Edit Glob Grep WebSearch WebFetch \
    --permission-mode dontAsk \
    --max-budget-usd "$BUDGET" \
    --output-format json > "$run/log.json" 2> "$run/errors.txt"
  code=$?

  mv "$brief" "inbox/done/$id.md"

  status="CRASHED (exit $code)"
  if [ -f "$run/status.md" ]; then status="$(head -n 1 "$run/status.md")"; fi
  if ! python3 scripts/check_run.py "$run" > "$run/check.txt" 2>&1; then
    status="$status, CHECK FAILED"
  fi
  echo "- $(date '+%Y-%m-%d %H:%M') | $status | $run" >> runs/MORNING.md
  echo "  $status"
done

echo "Done. Read runs/MORNING.md"
