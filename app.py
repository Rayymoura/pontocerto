"""PontoCerto - servidor Flask (local e Vercel).

Os dados vivem no localStorage do navegador (offline-first) e são
sincronizados com o Supabase quando há internet.
"""
import os
from pathlib import Path

from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent

# Carrega .env local (sem dependência extra)
env_file = BASE_DIR / ".env"
if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

app = Flask(__name__, template_folder=str(BASE_DIR / "templates"), static_folder=str(BASE_DIR / "static"))


@app.get("/")
def index():
    return render_template(
        "index.html",
        supabase_url=os.environ.get("SUPABASE_URL", ""),
        supabase_key=os.environ.get("SUPABASE_ANON_KEY", ""),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
