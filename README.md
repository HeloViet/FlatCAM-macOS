# FlatCAM macOS custom build

This repository tracks the FlatCAM Evo application source and the macOS-specific
changes used by the local Homebrew installation.

It intentionally does not include the Python runtime, Homebrew dependencies,
compiled libraries, or virtual-environment metadata. Those remain managed by
Homebrew on the Mac.

## Local changes

- Python 3.11 compatibility fix in the NCC plugin.
- Non-native file dialogs and macOS crash workarounds.
- Fixed working directory: `~/Documents/FlatCAM-files`.
- Disabled automatic project-tree expansion that crashes Qt on macOS.
- Default spindle soft-start: `M03 S250`, `G04 P3`, then target speed.

## Source

FlatCAM Evo is MIT-licensed. The original copyright and license notices are
retained with the source files.
