"""Launch the Streamlit app when run as main."""
from pathlib import Path
import sys

if __name__ == "__main__":
    app_path = Path(__file__).resolve().parent / "app.py"
    sys.argv = ["streamlit", "run", str(app_path)]
    import streamlit.web.cli as stcli
    stcli.main()