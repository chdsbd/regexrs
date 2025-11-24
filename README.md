# regex-rust (regexrs)

For of [regex-rust](https://github.com/spyoungtech/regexrs) updated for use in Kodiak. Not for general consumption.

## Building Wheels

```bash
uv run maturin build --release --target universal2-apple-darwin
docker run --rm -v $(pwd):/io ghcr.io/pyo3/maturin build --release --interpreter 3.11 3.12 3.13 3.14
```
