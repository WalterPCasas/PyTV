<?php

	$content = file_get_contents("http://ultimosismo.igp.gob.pe/");
	// echo $content;

	preg_match_all("|<[^>]+>(.*)</[^>]+>|U", $content, $cap );
		
	// var_export($cap);

	/*** Reporte Sísmico ***/
	// print_r($cap[0][9]);



	// Parametros hipocentrales

	print_r($cap[0][26]);  // Fecha Local
	print_r($cap[0][28]);  // Hora Local
	print_r($cap[0][30]);  // Latitud
	print_r($cap[0][32]);  // Longitud
	print_r($cap[0][34]);  // Profundidad
	print_r($cap[0][36]);  // Referencia
	print_r($cap[0][38]);  // Magnitud
	print_r($cap[0][40]);  // Intensidad
	print_r($cap[0][42]);  // Fecha UTC
	print_r($cap[0][44]);  // Hora UTC

	/*** Generación de XML ***/
	$xml = new DomDocument('1.0', 'UTF-8'); 
	
	$root = $xml->createElement('alerta'); 
	$root = $xml->appendChild($root); 

	$colaborador=$xml->createElement('identificador', 'INDECI'); 
	$colaborador =$root->appendChild($colaborador);

	$fechaHora=$xml->createElement('fechaHora', $cap[0][42].'T'.$cap[0][44]); 
	$fechaHora =$root->appendChild($fechaHora);


	$xml->formatOutput = true;
 
	$strings_xml = $xml->saveXML();
	$xml->save('/home/notfound/Documents/Work/Inictel/ejemplo.xml'); 

	echo "<br><br>Listo!!";

