#!/usr/bin/env bash
# Daily toolbox refresh: live GitHub numbers → data/tools.json → README → push.
# Output is delivered verbatim (cron no_agent), so keep it short and human.
set -uo pipefail
cd /opt/data/workspace/toolbox-repo || { echo "toolbox: repo missing"; exit 1; }

OUT=$(/opt/data/skills/.venv/bin/python tools/verify.py --push 2>&1)
RC=$?

CHANGES=$(printf '%s\n' "$OUT" | sed -n '/change(s):/,/entries,/p' | grep '~' || true)
TOTAL=$(printf '%s\n' "$OUT" | grep -oE '^[0-9]+ entries' | head -1)
PUSH=$(printf '%s\n' "$OUT" | grep -E '^(pushed|push failed)$' | head -1)

if [ -n "$CHANGES" ]; then
  N=$(printf '%s\n' "$CHANGES" | wc -l)
  echo "🗃 toolbox — امروز $N تغییر ($TOTAL)${PUSH:+, $PUSH}"
  printf '%s\n' "$CHANGES" | sed 's/^  ~ /• /' | head -12
  echo "https://github.com/ahmadvahidi/toolbox"
else
  echo "🗃 toolbox — بدون تغییر ($TOTAL)${PUSH:+ · $PUSH}"
fi

# A non-zero exit means the numbers could not be read at all; say so loudly.
if [ $RC -ne 0 ]; then
  echo "⚠️ refresh failed (rc=$RC)"
  printf '%s\n' "$OUT" | tail -3
fi
