#!/usr/bin/env python3
"""Install a PreTeXt wrapper that prepares the Runestone fallback cache.

PreTeXt 2.44.0 ships its fallback XML as ``runestone_services.xml`` but the
runtime looks for ``rs_services.xml``. When the Runestone CDN is unavailable,
the missing alias turns a recoverable network failure into an unbound-local
error. The central release workflow invokes this validation hook before
installing build dependencies, so the hook installs a small wrapper first; the
wrapper prepares the cache only when the ``pretext`` command is later called.
"""

from __future__ import annotations

import os
from pathlib import Path


WRAPPER = r'''#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import shutil
import xml.etree.ElementTree as ET

import pretext.resources

cache_dir = pretext.resources.resource_base_path() / "rs_cache"
bundled_xml = cache_dir / "runestone_services.xml"
cached_xml = cache_dir / "rs_services.xml"

if not cached_xml.exists():
    if not bundled_xml.is_file():
        raise SystemExit(f"PreTeXt cache XML não encontrado: {bundled_xml}")
    root = ET.parse(bundled_xml).getroot()
    version = root.findtext("./version")
    if not version:
        raise SystemExit(f"Versão dos serviços Runestone ausente em: {bundled_xml}")
    archive = cache_dir / f"dist-{version}.tgz"
    if not archive.is_file():
        raise SystemExit(f"Arquivo de serviços Runestone não encontrado: {archive}")
    shutil.copyfile(bundled_xml, cached_xml)
    print(f"Cache Runestone preparado: {cached_xml.name} (v{version})")
PY

exec python -m pretext "$@"
'''


def install_wrapper() -> None:
    repository = Path(__file__).resolve().parents[1]
    wrapper_dir = Path(
        os.environ.get(
            "REALMAT_PRETEXT_WRAPPER_DIR",
            repository / ".realmat" / "pretext-wrapper",
        )
    )
    wrapper_dir.mkdir(parents=True, exist_ok=True)
    wrapper = wrapper_dir / "pretext"
    wrapper.write_text(WRAPPER, encoding="utf-8")
    wrapper.chmod(0o755)

    github_path = os.environ.get("GITHUB_PATH")
    if github_path:
        with open(github_path, "a", encoding="utf-8") as path_file:
            path_file.write(f"{wrapper_dir}\n")
    print(f"Wrapper PreTeXt preparado: {wrapper}")


if __name__ == "__main__":
    install_wrapper()
