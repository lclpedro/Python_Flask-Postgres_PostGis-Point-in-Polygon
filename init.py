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

