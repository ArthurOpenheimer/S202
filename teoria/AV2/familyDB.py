class FamilyDB:
    
    def __init__(self, database):
        self.db = database

    def get_parents(self, nome):
        query = f"MATCH (p:Pessoa)-[:PAI_DE]->(c:Pessoa {{nome: '{nome}'}}) RETURN p"
        results = self.db.execute_query(query)
        return [result['p']['nome'] for result in results]

    def get_siblings(self, nome):
        query = f"MATCH (p:Pessoa)-[:IRMAO_DE]->(c:Pessoa {{nome: '{nome}'}}) RETURN p"
        results = self.db.execute_query(query)
        return [result['p']['nome'] for result in results]

    def get_relationship(self, nome):
        #busca: Luana namora com quem desde quando?
        #fazer o match retornar o nome e a data de inicio do relacionamento (propriedade do relacionamento)
        query = f"MATCH (p:Pessoa {{nome: '{nome}'}})-[r:NAMORADO_DE]->(c:Pessoa) RETURN c, r"
        results = self.db.execute_query(query)
        return [(result['c']['nome'], result['r']['desde']) for result in results]