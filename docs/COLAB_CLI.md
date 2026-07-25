# Working with Colab from the terminal (Colab CLI)

Google's official **Colab CLI** (released June 2026) lets us provision Colab
GPUs/TPUs and run our repo's scripts/notebooks from the terminal — so heavy model
training stays reproducible and version-controlled, instead of living in a browser tab.

- GitHub: https://github.com/googlecolab/google-colab-cli
- Supported OS: **Linux & macOS only** (WSL2 counts as Linux). Not Windows-native.

## When we use what

| Task | Tool |
|------|------|
| Learning weeks (1–2), interactive lessons | **Browser Colab** — better for a beginner |
| Heavy GPU training (weeks 3–5), reproducible runs | **Colab CLI** from this repo |

## Install (already done on this machine)

Installed into a dedicated venv and symlinked onto PATH (avoids Debian PEP 668 issues):

```bash
python3 -m venv ~/.local/share/colab-cli-venv
~/.local/share/colab-cli-venv/bin/pip install --upgrade pip google-colab-cli
ln -sf ~/.local/share/colab-cli-venv/bin/colab ~/.local/bin/colab
```

To update later: `~/.local/share/colab-cli-venv/bin/pip install --upgrade google-colab-cli`

## First-time authentication (run once, interactively)

```bash
colab new -s test        # CPU runtime (no --gpu) = cheapest; triggers Google OAuth login
```

Credentials cache to `~/.config/colab-cli/`. After this, no repeated logins.

## Everyday commands

```bash
# Provision a GPU session (availability depends on Colab subscription tier)
colab new -s work --gpu L4          # options: T4, L4, G4, A100, H100

# Put packages on the VM
colab install -s work numpy scikit-learn matplotlib

# Push our code up, run it, pull results back
colab upload   -s work src/ src/
colab exec     -s work -f src/train_model.py
colab download -s work results/ results/

# Interactive when needed
colab repl -s work                  # Python REPL on the VM
colab console -s work               # raw shell

# Save the session history as a notebook or markdown (nice for the write-up)
colab log -s work -o results/run_log.ipynb

# Always tear down when finished (stops burning compute units)
colab stop -s work
```

### One-shot jobs (provision → run → auto teardown)

```bash
colab run --gpu L4 src/train_model.py
```

## Cost note

GPU/TPU sessions consume Colab compute units. Use **CPU sessions** (omit `--gpu`) for
testing, prefer smaller GPUs (T4/L4) over A100/H100 unless needed, and **always
`colab stop`** when done.
