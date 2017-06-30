## Python_Flask-Postgres_PostGis-Point-in-Polygon
Point in Polygon | Python e Flask PostgreSQL Postgis

Database

```
+------------------------------------------------------------+
|id_localidade | nome       | poligono    | activate         |
--------------------------------------------------------------
|      1       |   Teste    | <geometria> |      True        |
--------------------------------------------------------------
```
#### Teste
```python
@app.route('/api/localidade/point=[<latitude>,<longitude>]', methods=['GET'])
def verifica_ponto_in_poligono(latitude, longitude):
	local=[]
	query="SELECT id_localidade,nome, poligono FROM localidade WHERE ST_Intersects('POINT("+latitude+" "+longitude+" )'::geometry, poligono) and activate='True'"
	listalocalidades=db.engine.execute(query)
	for und in listalocalidades:
		localidade = {
			'id_localidade':und.id_localidade,
			'nome':und.nome
		}
		local.append(localidade)
	return jsonify(local)
  
#Executa Função passando parametros
verifica_ponto_in_poligono(-67.8519809246063,-9.96074206300764)



```

Se o ponto passado na função existir, retornará o resultado:
```json
[
    {
        "id_localidade": 1,
        "nome": "Teste"
    }
]
```
Se não
```json
[]
```

