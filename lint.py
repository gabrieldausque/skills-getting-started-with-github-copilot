#!/usr/bin/env python3
"""
Pylint runner script for the Mergington High School project.
Run this script to check code quality across all Python files.
"""

import subprocess
import sys
from pathlib import Path

def run_pylint():
    """Run pylint on all Python files in the src directory."""
    project_root = Path(__file__).parent
    src_dir = project_root / "src"

    if not src_dir.exists():
        print("Error: src directory not found!")
        return 1

    # Find all Python files in src directory
    python_files = list(src_dir.glob("**/*.py"))

    if not python_files:
        print("No Python files found in src directory!")
        return 1

    print(f"Running pylint on {len(python_files)} Python files...")

    # Run pylint on each file
    overall_success = True
    for py_file in python_files:
        print(f"\nChecking {py_file.relative_to(project_root)}...")
        try:
            result = subprocess.run(
                ["pylint", str(py_file)],
                capture_output=True,
                text=True,
                cwd=project_root
            )

            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"Stderr: {result.stderr}")

            # Pylint returns 0 for perfect score, non-zero for issues
            if result.returncode != 0:
                overall_success = False

        except FileNotFoundError:
            print("Error: pylint not found. Make sure it's installed: pip install pylint")
            return 1
        except Exception as e:
            print(f"Error running pylint: {e}")
            return 1

    if overall_success:
        print("\n✅ All files passed pylint checks!")
        return 0
    else:
        print("\n⚠️  Some files have pylint issues to address.")
        return 1

if __name__ == "__main__":
    sys.exit(run_pylint())
