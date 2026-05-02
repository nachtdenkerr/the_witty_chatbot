"""
Running submitted code from user and evaluate
"""

import os
import subprocess

def run_code(code: str) -> str:
    """
    Run code
    """
    path = os.path.join(os.getcwd(), "temp")
    file_name = "temp.py"
    with open(os.path.join(path, file_name), "w", encoding="utf-8") as temp_file:
        temp_file.write(code)
        temp_file.close()
    try:
        result = subprocess.run(["python", os.path.join(path, file_name)],
                            capture_output=True, text=True, check=False, timeout=10)
    except subprocess.TimeoutExpired:
        return ("timeout", "", "subprocess.TimeoutExpired")
    except Exception:
        return ("internal_error", "", "Might be system failure")
    
    return ("success" if result.returncode == 0 else "failure", result.stdout, result.stderr)
