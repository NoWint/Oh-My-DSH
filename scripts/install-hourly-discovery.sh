#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PLIST="$HOME/Library/LaunchAgents/com.oh-my-dsh.discovery.plist"
ENV_FILE=${2:-"$ROOT/.env"}
case "${1:-check}" in
  check)
    [ -f "$ENV_FILE" ] || { echo "missing env file: $ENV_FILE" >&2; exit 1; }
    mode=$(stat -f '%Lp' "$ENV_FILE" 2>/dev/null || stat -c '%a' "$ENV_FILE")
    [ "$mode" = 600 ] || { echo "env file must be mode 0600" >&2; exit 1; }
    echo "ok"
    ;;
  install)
    "$0" check "$ENV_FILE"
    mkdir -p "$(dirname "$PLIST")"
    sed "s|__ROOT__|$ROOT|g; s|__ENV_FILE__|$ENV_FILE|g" "$ROOT/launchd/com.oh-my-dsh.discovery.plist.template" > "$PLIST"
    launchctl load "$PLIST"
    ;;
  uninstall)
    launchctl unload "$PLIST" 2>/dev/null || true
    rm -f "$PLIST"
    ;;
  *) echo "usage: $0 {install|uninstall|check} [env-file]" >&2; exit 2 ;;
esac
