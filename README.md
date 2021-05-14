# Bazel Boilerplate

This project evaluates Bazel for a multi-language monorepo, starting with Python/ProtoBuf.

## Features (what works, what doesn't work yet)

Done:

- [x] Build `py_library` for packages `foo` and `bar`
- [x] Build/run `py_binary`
- [x] Build/run executable Python `.zip` file for `foo` binary
- [x] Run unit tests
- [x] Depend on 3rd party PyPI dependency `numpy` in `bar` package
- [x] 3rd party dependency resolution test/update using `compile_pip_requirements` (in `third_party/python`)

Next steps:

- [ ] Import members of package `bar` in package `foo` via `from bar import ...` (not `from src.python.bar import ...`)
- [ ] Build `.whl`
- [ ] Compile `.proto` messages with Bazel
- [ ] Docker image
- [ ] Vendor Python interpreter

## Build/run `py_binary`

- Run through Bazel
    ```bash
    ./bazelisk run //src/python/foo:foo_bin
    ```
- Build and run manually
    ```bash
    ./bazelisk build //src/python/foo:foo_bin
    ./bazel-bin/src/python/foo/foo_bin
    ```
- Build and run Python zip
    ```bash
    ./bazelisk build //src/python/foo:foo_bin --build_python_zip
    python3 ./bazel-bin/src/python/foo/foo_bin.zip
    ```

## Build all targets

```bash
./bazelisk build ...
```

## Run all tests

```bash
./bazelisk test ...
```

## Update `requirements.txt`

```bash
./bazelisk run //third_party/python:requirements.update
```

## Delete caches

```bash
./bazelisk clean --expunge
```
