# iitech-jfrog-multipypi-demo

Demo Python package for validating publishing to JFrog Artifactory (JFrog Cloud) and installing via a Virtual PyPI repository.

## Configure ~/.netrc (developer machines)

Create `~/.netrc` with your Artifactory credentials (token preferred):

```text
machine iitech.jfrog.io
  login YOUR_USERNAME
  password YOUR_ACCESS_TOKEN
```

Set safe permissions:

```sh
chmod 600 ~/.netrc
```

## Install via Artifactory Virtual PyPI

Note: the `/simple` suffix is required for pip's simple API.

```sh
pip install --index-url https://iitech.jfrog.io/artifactory/api/pypi/pypi-virtual/simple iitech-jfrog-multipypi-demo
```

## Publish via Git tag

Publishing is handled by the GitHub Actions tag workflow. Create and push a semver tag:

```sh
git tag v0.1.0 && git push origin v0.1.0
```

The workflow extracts the version from the tag, updates `pyproject.toml`, builds the package, and uploads to `pypi-local`.
