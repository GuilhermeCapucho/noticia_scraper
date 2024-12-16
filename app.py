from flask import Flask, render_template, request, send_file
import json
import pandas as pd
import os
from scraper import coletar_noticias

app = Flask(__name__)

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open('config.json') as f:
    config = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', sites=config.keys())

@app.route('/scrape', methods=['POST'])
def scrape():
    site = request.form['site']
    site_config = config[site]
    url = site_config["base_url"]
    paginas = int(request.form['paginas'])

    noticias = coletar_noticias(url, site_config, limite_paginas=paginas)

    if noticias:
        df = pd.DataFrame(noticias)
        base_name = f"noticias_{site}"
        csv_path = os.path.join(OUTPUT_DIR, f"{base_name}.csv")
        json_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")
        excel_path = os.path.join(OUTPUT_DIR, f"{base_name}.xlsx")

        df.to_csv(csv_path, index=False)
        df.to_json(json_path, orient='records', indent=4)
        df.to_excel(excel_path, index=False)

        return render_template('resultados.html', noticias=noticias, site=site, base_name=base_name)
    else:
        return render_template('resultados.html', noticias=None, site=site, base_name=None)

@app.route('/download/<format>/<base_name>')
def download(format, base_name):
    file_path = None

    if format == "csv":
        file_path = os.path.join(OUTPUT_DIR, f"{base_name}.csv")
    elif format == "json":
        file_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")
    elif format == "excel":
        file_path = os.path.join(OUTPUT_DIR, f"{base_name}.xlsx")

    if file_path and os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"Arquivo {file_path} não encontrado.", 404

if __name__ == '__main__':
    app.run(debug=True)