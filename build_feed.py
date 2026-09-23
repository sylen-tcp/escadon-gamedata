#!/usr/bin/env python3
"""Build the integrity-wrapped Escadon volatile feed.

Developer-side utility only. End users never run this.
Input is a payload JSON containing format/revision/builds. Output is the exact
`latest.json` consumed by Escadon 20.4.0.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("payload", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=Path("latest.json"))
    ns = ap.parse_args()
    payload_obj = json.loads(ns.payload.read_text(encoding="utf-8"))
    if payload_obj.get("format") != 1 or not isinstance(payload_obj.get("builds"), list):
        raise SystemExit("payload must contain format=1 and builds[]")
    payload = json.dumps(payload_obj, separators=(",", ":"), ensure_ascii=False)
    envelope = {
        "format": 1,
        "payload": payload,
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    }
    ns.output.write_text(json.dumps(envelope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(ns.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
