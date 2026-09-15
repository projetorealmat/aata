#!/usr/bin/env python3
"""Make PreTeXts bundled Runestone fallback usable in offline CI.

PreTeXt 2.44.0 ships its fallback XML as ``runestone_services.xml`` but the
runtime looks for ``rs_services.xml``. When the Runestone CDN is unavailable,
the missing alias turns a recoverable network failure into an unbound-local
error. Keep the bundled XML and archive together, and only create the alias
when PreTeXt has not already populated a fresher cache from the CDN.
"""

from __future__ import annotations

import shutil
import xml.etree.ElementTree as ET

import pretext.resources


def prepare_cache() -> None:
    cache_dir = pretext.resources.resource_base_path() / "rs_cache"
    bundled_xml = cache_dir / "runestone_services.xml"
    cached_xml = cache_dir / "rs_services.xml"

    if cached_xml.exists():
        return
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


if __name__ == "__main__":
    prepare_cache()
