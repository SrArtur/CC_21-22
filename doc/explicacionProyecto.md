# Descripción del problema
Cada verano la Guardia Civil ante la previsión del aumento de puestos de trabajo alerta sobre las ofertas de empleo fraudulentas. Este hecho se ve reflejado en una época 'post-pandemica' de salida de una crisis, en la que hay un incremento de un 35% respecto a 2019 en ofertas trabajo según FashionUnited. Ante la situación de inestabilidad laboral que se presenta, los ciberdelincuentes aprovechan para pasar más desapercibidos entre el aluvión de ofertas.

Recurrir a falsas oportunidades puede hacer que los estafadores puedan recopilar datos personales o incluso pedir dinero a cambio para supuestos gastos de gestión.


# Solución propuesta

Hay recomendaciones para diferenciar entre ofertas reales o falsas como puede ser el uso de teléfonos de tarificación especial, opción de teletrabajo para puesto manuales, condiciones demasiado atractivas, mala redacción, etc.

Como toda precaución es poca, para resolver este problema se propone una aplicación web en la que los usuarios puedan introducir una oferta y la aplicación predecir si dicha oferta es falsa según varios indicativos como los mencionados anteriormente. Para poder predecir se usarán los datos de [University of the Aegean](http://emscad.samos.aegean.gr/) y técnicas de _Machine Learning_, más concretamente aprendizaje supervisado. Este banco de datos contiene en torno a 19 mil ofertas de trabajo, de las cuales, en torno a 800 son falsas.

Además se podrán reportar ofertas de empleo falsas para así ir mejorando el algoritmo.

Finalmente, resulta de interés el reentrenamiento de dicho algoritmo con los nuevos datos de ofertas falsas que se vayan reportando para así ir detectando las tendencias de los estafadores. 

Podrás acceder al sistema desde distintos dispositivos, ya que toda la información  y gestión se guardará y hará en la nube.

# Documentación adicional

Puedes consultar las fuentes acerca de los datos en los siguientes enlaces:
  - [Falsa Ofertas de empleo](https://www.osi.es/es/falsas-ofertas-empleo)
  - [Aumento de ofertas de empleo fraudulentas](https://www.portalparados.es/actualidad/la-guardia-civil-alerta-del-aumento-de-ofertas-de-empleo-fraudulentas/)
  - [Aumento de las ofertas de trabajo](https://fashionunited.es/noticias/empresas/aumento-del-35-de-las-ofertas-de-trabajo-en-comparacion-con-la-epoca-anterior-a-la-crisis/2021100436494)