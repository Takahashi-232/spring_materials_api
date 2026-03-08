from flask import Flask, render_template
from materials.spring_material_db import SpringMaterialDB

app = Flask(__name__)

# --- ばね材料データベースを読み込む ---
db = SpringMaterialDB()
spring_materials = db.DATA   # ← ここを DATA に変更！


@app.get("/")
def index():
    return "Flask が動いています！"


@app.get("/spring_materials")
def spring_materials_page():
    return render_template(
        "spring_materials.html",
        spring_materials=spring_materials
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)