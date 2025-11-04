#!/usr/bin/env python3
import subprocess
import sys

if __name__ == "__main__":
    result = subprocess.run(["behave", "features/main_page.feature"],
                          capture_output=False)
    sys.exit(result.returncode)