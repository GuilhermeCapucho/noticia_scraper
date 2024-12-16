import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def coletar_noticias(url, site_config, limite_paginas=0):
    todas_noticias = []
    paginas_coletadas = 0

    while paginas_coletadas < limite_paginas:
        try:
            print(f"Acessando {url}")
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"Erro ao acessar {url}: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')

            noticias = soup.find_all(site_config["link_tag"], class_=site_config["title_class"])

            for item in noticias:
                try:
                    titulo = ''.join(item.stripped_strings)
                    date_tag = item.find_next('span', class_=site_config.get("date_class"))
                    if date_tag:
                        data_text = date_tag.get_text(strip=True)
                        titulo = titulo.replace(data_text, '').strip()

                    link = item['href']
                    if link.startswith('/'):
                        link = site_config["base_url"].rstrip('/') + link

                    data = data_text if date_tag else "Sem data"

                    todas_noticias.append({
                        "Título": titulo,
                        "Link": link,
                        "Data": data
                    })
                except Exception as e:
                    print(f"Erro ao processar item: {e}")

            paginas_coletadas += 1

            if paginas_coletadas < limite_paginas:
                url = site_config["pagination_url"].format(paginas_coletadas + 1)
            else:
                break

        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            break
    return todas_noticias

def salvar_dados(df, formatos=["csv", "excel", "json"]):
    if "csv" in formatos:
        try:
            df.to_csv('noticias.csv', index=False)
            print("Arquivo CSV salvo como 'noticias.csv'")
        except Exception as e:
            print(f"Erro ao salvar CSV: {e}")

    if "excel" in formatos:
        try:
            df.to_excel('noticias.xlsx', index=False)
            print("Arquivo Excel salvo como 'noticias.xlsx'")
        except Exception as e:
            print(f"Erro ao salvar Excel: {e}")

    if "json" in formatos:
        try:
            df.to_json('noticias.json', orient='records', indent=4)
            print("Arquivo JSON salvo como 'noticias.json'")
        except Exception as e:
            print(f"Erro ao salvar JSON: {e}")

if __name__ == "__main__":
    with open('config.json') as f:
        config = json.load(f)

    site = "cnn"
    site_config = config[site]
    url = site_config["base_url"]

    todas_noticias = coletar_noticias(url, site_config, limite_paginas=2)

    if todas_noticias:
        df = pd.DataFrame(todas_noticias)
        df['Link'] = df['Link'] + " "
        
        salvar_dados(df, formatos=["csv", "excel", "json"])
    else:
        print("Nenhuma notícia foi encontrada.")