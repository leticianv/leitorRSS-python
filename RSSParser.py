import feedparser
from time import gmtime


class RssParser():
    url = ""
    
    def __init__(self, rss_url):
        print(f"URL RSS: {rss_url}")
        self.url = rss_url
        self.detalhes_conteudo = {}
        self.noticias = []
        self.parse()

    def parse(self):
        artigos = feedparser.parse(self.url)
        self.detalhes_conteudo['titulo'] = artigos.feed.get('title', '')
        self.detalhes_conteudo['descricao'] = artigos.feed.get('description', '')
        self.detalhes_conteudo['quantidade_noticias'] = len(artigos.entries)
        
        self.noticias = artigos.entries