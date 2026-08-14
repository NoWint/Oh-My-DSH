#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
LABEL=com.oh-my-dsh.discovery
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
ENV_FILE=${2:-"$ROOT/.env"}
check_env() {
  [ -f "$ENV_FILE" ] && [ ! -L "$ENV_FILE" ] || { echo "env file must be regular" >&2; exit 1; }
  # Cross-platform: use python3 for stat (macOS stat -f differs from Linux stat -c)
  python3 -c "
import os, sys
p = sys.argv[1]
uid = os.stat(p).st_uid
mode = os.stat(p).st_mode & 0o777
assert uid == os.getuid(), 'env file must be owned by current user'
assert mode == 0o600, 'env file must have mode 0600'
" "$ENV_FILE" || { echo "env file validation failed" >&2; exit 1; }
}
case "${1:-check}" in
 check) check_env; echo ok ;;
 install)
  check_env
  mkdir -p "$(dirname "$PLIST")"
  ROOT="$ROOT" ENV_FILE="$ENV_FILE" PLIST="$PLIST" python3 - <<'PY'
import os
from pathlib import Path
text=(Path(os.environ['ROOT'])/'launchd/com.oh-my-dsh.discovery.plist.template').read_text()
text=text.replace('__ROOT__', os.environ['ROOT']).replace('__ENV_FILE__', os.environ['ENV_FILE'])
path=Path(os.environ['PLIST']); path.write_text(text); path.chmod(0o600)
PY
  plutil -lint "$PLIST"
  launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$PLIST"
 ;;
 uninstall) launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true; rm -f "$PLIST" ;;
 *) echo "usage: $0 {install|uninstall|check} [env-file]" >&2; exit 2 ;;
esac
