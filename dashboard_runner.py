import sys
import os
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "src/dashboard.py"]
sys.exit(stcli.main())
