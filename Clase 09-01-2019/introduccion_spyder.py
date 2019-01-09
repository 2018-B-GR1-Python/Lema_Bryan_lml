import scrapy
nombre_archivo = 'book_information.csv'
class IntroSpider(scrapy.Spider):  
  nombre = 'introduccion_spider'
  
  def start_requests(self): 
    urls = [
      'http://books.toscrape.com/catalogue/page-1.html',
      'http://books.toscrape.com/catalogue/page-2.html',
      'http://books.toscrape.com/catalogue/page-3.html',
      'http://books.toscrape.com/catalogue/page-4.html',
      'http://books.toscrape.com/catalogue/page-5.html',
    ]
    
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)
    
  def parse(self,response):
    lista_libros = response.css('article.product_pod > h3 > a::attr(title)').extract()
    lista_precios = response.css('article.product_pod > div > p::text').extract()
    lista_disponible = response.css('article.product_pod.product_price > p::text').extract()
    
    with open(nombre_archivo, 'a+') as f:
      for aux in range(len(lista_libros)):
        f.write(lista_libros[aux]+','+lista_precios[aux]+','+comparar(lista_disponible[aux]))
  def comparar(texto):
    disponible = 0  
    if(texto.strip() == 'In stock'):
        disponible = 1
    return disponible