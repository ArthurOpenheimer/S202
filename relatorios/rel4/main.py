from database import Database
from productAnalyzer import ProductAnalyzer
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

analyzer = ProductAnalyzer(db)

analyzer.totalVendasDia()
analyzer.produtoMaisVendido()
analyzer.clienteMaiorGasto()
analyzer.produtosMaisDeUmaCompra()