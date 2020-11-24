
import json

def procesar_archivo(archivo):

	turnos = open(archivo, 'r', encoding="utf8", errors='ignore')
	objeto = turnos.readlines()
	textojson = ''
	for linea in objeto:
		textojson += linea

	turnos = json.loads(textojson)

	estados = {}

	for i in turnos:
		if 'status' in i:
			if i['status'] in estados:
				estados[i['status']].append(i)
			else:
				estados[i['status']] = [i]

		else:
			if 'errores' in estados:
				estados['errores'].append(i)
			else:
				estados['errores'] = [i]

	return(estados)

