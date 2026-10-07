"""Check that Python can drive PowerFactory 2024 through its API (engine mode, no GUI).

Run it with Python 3.12 (one of the versions PowerFactory 2024 supports), and close
the PowerFactory window first: engine mode starts its own PowerFactory session.
"""
import os
import sys

PF_DIR = r"C:\Program Files\DIgSILENT\PowerFactory 2024"
os.environ["PATH"] = PF_DIR + os.pathsep + os.environ["PATH"]
sys.path.append(os.path.join(PF_DIR, "Python", f"{sys.version_info.major}.{sys.version_info.minor}"))

import powerfactory as pf

try:
    app = pf.GetApplicationExt()
except pf.ExitError as e:
    sys.exit(f"PowerFactory did not start (error code {e.code})")

user = app.GetCurrentUser()
print("PowerFactory started in engine mode")
print("User:", user.loc_name)
print("Projects:", [p.loc_name for p in user.GetContents("*.IntPrj")])
