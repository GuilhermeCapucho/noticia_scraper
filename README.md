# Coletor Automático de Títulos e Links de Notícias - Notícia Scraper


Um projeto de **Web Scraper** desenvolvido em **Python** com o framework **Flask** para coletar notícias de sites específicos (atualmente: **CNN Brasil**) e salvar os resultados em **CSV**, **JSON** e **Excel**.

## **🚀 Funcionalidades**

- **Coleta de Notícias**: Extrai título, link e data das notícias.
- **Paginação**: Suporte para múltiplas páginas com URL paginada.
- **Exportação**: Salva os resultados em formatos **CSV**, **Excel** e **JSON**.
- **Interface Simples**: Interface web criada com Flask e HTML/CSS para facilitar o uso.

## **🔧 Pré-requisitos**

Para rodar o projeto, você precisa de:

- **Python 3.10+**
- **Pip** (gerenciador de pacotes do Python)

## **🔧 Tecnologias Usadas**

- **Python** (Linguagem principal)
- **Flask** (Backend e interface web)
- **BeautifulSoup4** (Scraping de dados)
- **Requests** (Requisições HTTP)
- **Pandas** (Manipulação de dados)
- **HTML/CSS** (Interface frontend)

## **📥 Instalação**

1. **Clone o repositório**:
    
    ```bash
    git clone https://github.com/seu-usuario/noticia_scraper.git
    cd noticia_scraper
    ```
    
2. **Instale as dependências**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Execute o projeto**:
    
    ```bash
    python app.py
    ```
    
4. **Abra no navegador**:
    
    ```bash
    http://127.0.0.1:5000/
    ```
    



## **⚙️ Configuração**

O arquivo **`config.json`** armazena as configurações dos sites suportados. Exemplo:

```json
{
    "CNN": {
        "base_url": "https://www.cnnbrasil.com.br/",
        "title_class": "home__list__tag",
        "link_tag": "a",
        "date_class": "home__title__date",
        "pagination_url": "https://www.cnnbrasil.com.br/noticias/pagina/{}/",
        "fetch_details": false}
}
```

- **`base_url`**: URL inicial do site.
- **`title_class`**: Classe CSS para localizar os títulos.
- **`pagination_url`**: Estrutura da URL para acessar as páginas paginadas.

## **🖥️ Como Usar**

1. Abra a aplicação no navegador.
2. Escolha o site desejado (**CNN Brasil**) e o número de páginas.
3. Clique em **"Iniciar Scraping"**.
4. Visualize as notícias na tabela e faça o download nos formatos desejados.

## **📊 Resultados**

Os resultados são salvos automaticamente na pasta `data` e estão disponíveis nos formatos:

- **CSV**: `noticias.csv`
- **Excel**: `noticias.xlsx`
- **JSON**: `noticias.json`

## **🛠️ Melhorias Futuras**

- Adicionar suporte para outros sites de notícias.
- Implementar autenticação e autorização.
- Adicionar filtros para palavras-chave específicas.
- Melhorar a interface com frameworks como Bootstrap.
