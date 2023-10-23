# Sleepless
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/toloco/sleepness/ci.yml)
![PyPI - Version](https://img.shields.io/pypi/v/sleepness)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sleepness)

[Sleepness in Pypi](https://pypi.org/project/sleepness/)

When you require an sleepless session, use **sleepless**.

Keep your screen on whilst you are drinking a ☕.

## INSTALLATION

On linux you'd need to have `Tkinter`, which is widely available in most distros.

Using public **pypi**:

```bash
pip install sleepness
```

```bash
pip3 install sleepness
```

Install from github:

```bash
pip install git+https://github.com/toloco/sleepness.git
```

## USAGE

```bash
sleepness --help
usage: sleepness [-h] [--timer TIMER] [--length [1-1000]] [--wait [10-1000]]

options:
  -h, --help         show this help message and exit
  --timer TIMER      Timer (in minutes), 0 means forever, default is forever.
  --length [1-1000]  Lenght of movement (in secs), default is 10.
  --wait [10-1000]   Waiting time between movements (in secs), default is 10.
```
