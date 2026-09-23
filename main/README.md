# Escadon volatile feed publisher

This folder is **developer-side only**. Distributed Escadon users do not need it.

`build_feed.py payload.json -o latest.json` produces the SHA-256 integrity envelope consumed by Escadon 20.4.0. Publish `latest.json` at the DLL's configured `ESCADON_VOLATILE_FEED_URL`.

Each build entry must use the exact fingerprint emitted for `client.dll`, `engine2.dll`, and `inputsystem.dll`. A non-matching build is ignored by the DLL. Signature and pattern overrides are still unique-scan/address validated when used.
