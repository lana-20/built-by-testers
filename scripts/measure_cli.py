#!/usr/bin/env python3
"""
Measure Vibium CLI performance on built-by-testers creator sites.

Usage:
  python3 measure_cli.py <site_url> [--output results.csv]

Example:
  python3 measure_cli.py https://testers.ai/testing --output cli_results.csv

This script:
1. Captures baseline token count
2. Runs vibium CLI commands on the specified site
3. Records timing, element count, and token delta
4. Saves results to CSV for comparison with MCP measurements
"""

import subprocess
import time
import json
import sys
import os
from pathlib import Path
import csv

def capture_baseline():
    """Capture current message ID from Claude session JSONL."""
    try:
        result = subprocess.run(
            "jq '.messages[-1].id' ~/.claude/projects/**/*.jsonl 2>/dev/null | tail -1",
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Warning: Could not capture baseline: {e}")
        return "0"

def measure_site(url: str, timeout: int = 60) -> dict:
    """
    Measure a site using vibium CLI with bracket protocol v2.

    Returns dict with timing, element count, and workflow info.
    """
    start_ms = time.time() * 1000

    try:
        # Ensure PATH includes vibium
        env = os.environ.copy()
        env['PATH'] = f"/usr/local/bin:{env.get('PATH', '')}"

        # Start browser
        subprocess.run(['vibium', 'start'], capture_output=True, timeout=10, env=env)
        time.sleep(1)

        # Navigate to site
        subprocess.run(['vibium', 'go', url], capture_output=True, timeout=timeout, env=env)
        time.sleep(2)

        # Map elements
        result = subprocess.run(['vibium', 'map'], capture_output=True, text=True, timeout=10, env=env)
        element_count = result.stdout.count('@e')

        end_ms = time.time() * 1000
        duration = int(end_ms - start_ms)

        # Stop browser
        subprocess.run(['vibium', 'stop'], capture_output=True, timeout=5, env=env)

        return {
            'duration_ms': duration,
            'elements': element_count,
            'status': 'success'
        }
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'duration_ms': int(time.time() * 1000 - start_ms)}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    url = sys.argv[1]
    output_file = 'cli_results.csv'

    # Parse arguments
    if '--output' in sys.argv:
        idx = sys.argv.index('--output')
        if idx + 1 < len(sys.argv):
            output_file = sys.argv[idx + 1]

    print(f"Measuring CLI performance on: {url}")
    print(f"Output file: {output_file}")
    print()

    # Capture baseline
    baseline = capture_baseline()
    print(f"Baseline token ID: {baseline}")

    # Run measurement
    result = measure_site(url)
    print(f"Result: {json.dumps(result, indent=2)}")

    # Capture final token count
    final = capture_baseline()
    turns = int(final) - int(baseline) if baseline and final else 0

    # Save to CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'cli_ms', 'elements', 'turns', 'status'])
        writer.writeheader()
        writer.writerow({
            'url': url,
            'cli_ms': result.get('duration_ms', 0),
            'elements': result.get('elements', 0),
            'turns': turns,
            'status': result.get('status', 'unknown')
        })

    print(f"\nResults saved to {output_file}")

if __name__ == '__main__':
    main()
