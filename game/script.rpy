define l = Character("Luna", color="#66ccff")
define e = Character("Don Ernesto", color="#996633")
define s = Character("Sofía", color="#cc6699")
define v = Character("Sr. Vargas", color="#999999")
define n = Character(None)  


define maria = Character("Vecina María", color="#a3c586")
define carlos = Character("Vecino Carlos", color="#6ca0dc")


image bg river_morning = "rio3.png"
image bg plaza_day = "plaza.jpg"
image bg river_polluted = "rio_malo.jpg"
image bg river_mixed = "rio4.jpg"


image luna neutral = "luna3.png"
image luna neutral_dark = "luna_dark.png"
image ernesto neutral = "ernesto3.png"
image ernesto neutral_dark = "ernesto_dark.png"
image sofia neutral = "sofia3.png"
image vargas neutral = "vargas_neutral.png"

image vecina_maria normal = "vecina3.png"
image vecino_carlos normal = "vecino3.png"


default decision_accion = 0  
default apoyo_comunidad = 0  

label start:

    scene bg river_morning with fade




    n "Un pequeño pueblo junto a un río que ha sido fuente de vida por generaciones. Pero algo está cambiando."

    show luna neutral at left with dissolve

    l "Este río siempre fue nuestro orgullo. Pero ahora el agua no es la misma. Los peces desaparecen y el olor es extraño."

    show ernesto neutral at right with dissolve

    e "He vivido aquí toda la vida y nunca vi el río así. La fábrica trajo trabajo, sí, pero también problemas que no podemos ignorar."

    show sofia neutral at center with dissolve

    s "Soy Sofía, ingeniera ambiental. Vine para investigar qué está pasando y ayudar si es posible."

    menu:
        "¿Qué quieres hacer primero?"
        "Preguntar a Don Ernesto sobre los cambios en el río":
            jump preguntar_ernesto
        "Investigar la fábrica y sus actividades":
            jump investigar_fabrica
        "Hablar con otros vecinos para conocer sus opiniones":
            jump hablar_vecinos

label preguntar_ernesto:

    l "Don Ernesto, ¿qué cambios has notado en el río?"

    e "Antes el agua era clara y llena de vida. Ahora huele raro, y los peces mueren. La fábrica empezó a tirar residuos sin control."

    menu:
        "¿Qué quieres preguntarle?"
        "¿Has hablado con la fábrica?":
            e "Intentamos hablar, pero nos ignoran. Dicen que el progreso es más importante que el río."
        "¿Qué podemos hacer para detenerlo?":
            e "Organizar a la comunidad, juntar pruebas y exigir que cambien sus prácticas."

    jump decidir_accion

label investigar_fabrica:

    s "La fábrica parece no tener sistemas adecuados para tratar sus desechos. Esto explica la contaminación."

    menu:
        "¿Qué quieres hacer?"
        "Intentar hablar con el Sr. Vargas, dueño de la fábrica":
            jump hablar_vargas
        "Buscar documentos o denuncias previas":
            s "Encontré reportes de multas anteriores por contaminación, pero no se han aplicado sanciones efectivas."

    jump decidir_accion

label hablar_vargas:

    v "La fábrica da empleo a mucha gente. Entiendo las preocupaciones, pero el progreso es necesario."

    l "¿Estarías dispuesto a mejorar las prácticas para proteger el río?"

    v "Si la comunidad se une y exige cambios claros, podríamos considerar invertir en filtros."

    jump decidir_accion

label hablar_vecinos:

    scene bg plaza_day with fade

    n "En la plaza, escuchas opiniones divididas."

    show vecina_maria normal at left with dissolve
    maria "Muchos dependen de la fábrica, pero tememos por nuestra salud y el río."
    hide vecina_maria with dissolve

    show vecino_carlos normal at right with dissolve
    carlos "Sin la fábrica no hay trabajo. El río siempre ha cambiado, no creo que sea tan grave."
    hide vecino_carlos with dissolve

    menu:
        "¿Qué quieres hacer?"
        "Organizar una reunión comunitaria para unir voces":
            $ apoyo_comunidad = 2
            l "Debemos unirnos y exigir juntos un cambio."
            jump decidir_accion
        "Buscar apoyo externo, como autoridades o medios":
            $ apoyo_comunidad = 1
            s "Contactaré con autoridades ambientales y medios para visibilizar el problema."
            jump decidir_accion

label decidir_accion:

    menu:
        "¿Cómo quieres actuar para salvar el río?"
        "Negociar con la fábrica para que mejore sus prácticas":
            $ decision_accion = 1
            jump final_negociacion
        "Organizar una protesta para llamar la atención pública":
            $ decision_accion = 2
            jump final_protesta
        "Presentar una denuncia formal ante las autoridades ambientales":
            $ decision_accion = 3
            jump final_denuncia

label final_negociacion:

    scene bg plaza_day with fade

    show vargas neutral at center with dissolve
    show sofia neutral at left with dissolve
    show ernesto neutral at right with dissolve

    v "Reconozco que subestimamos el impacto. Invertiremos en tecnología para cuidar el río."

    s "Gracias a la presión social y el compromiso, la fábrica reducirá sus vertidos. Pero necesitamos seguir vigilando."

    e "El río vuelve a respirar. Esto es solo el comienzo, pero juntos podemos protegerlo."

    l "No fue fácil, pero valió la pena. El futuro depende de lo que hagamos hoy."

    if apoyo_comunidad == 2:
        n "La comunidad está unida y fuerte, trabajando para mantener el río limpio."
    elif apoyo_comunidad == 1:
        n "Con apoyo externo, la presión aumentó y la fábrica cedió."
    else:
        n "Aunque algunos dudaban, la negociación logró un cambio real."

    menu:
        "¿Quieres seguir trabajando en la educación ambiental o crear un comité de vigilancia?"
        "Campañas de educación ambiental":
            n "Organizan talleres y actividades para cuidar el río."
            jump end_good
        "Comité comunitario de vigilancia":
            n "La comunidad vigila que la fábrica cumpla sus compromisos."
            jump end_good

label end_good:
    n "El río renace gracias a la unión y compromiso de todos. Pero la vigilancia debe ser constante."
    return

label final_protesta:

    scene bg river_polluted with fade

    show luna neutral at left with dissolve
    show ernesto neutral at right with dissolve
    show sofia neutral at center with dissolve

    l "Lo intentamos todo, pero nadie nos escuchó. La fábrica sigue contaminando y el río se está muriendo."

    e "Perdimos la batalla. El río y nosotros pagamos el precio."

    s "Las leyes no se aplican, y la gente está cansada. Esto es solo el principio de un desastre mayor."

    show vargas neutral at center with dissolve

    v "El progreso no puede detenerse por un río. Si no les gusta, que se muden."

    if apoyo_comunidad == 0:
        n "La comunidad está dividida y sin fuerza para cambiar las cosas."
    elif apoyo_comunidad == 1:
        n "Aunque hubo apoyo externo, la fábrica ignoró las protestas."
    else:
        n "La protesta fue fuerte, pero no suficiente para detener la contaminación."

    menu:
        "¿Quieres buscar ayuda internacional o dejar el pueblo?"
        "Buscar apoyo internacional o ONG ambiental":
            n "Contactan organizaciones que comienzan a investigar y presionar."
            jump end_bad
        "Dejar el pueblo para buscar un futuro mejor":
            n "Luna decide irse, dejando atrás un río moribundo."
            jump end_bad

label end_bad:
    n "El río muere, y con él, una parte del pueblo. La lucha continúa, pero lejos de aquí."
    return

label final_denuncia:

    scene bg river_mixed with fade

    show sofia neutral at left with dissolve
    show luna neutral at center with dissolve
    show ernesto neutral at right with dissolve
    show vargas neutral at center with dissolve

    s "La fábrica instaló filtros y redujo sus vertidos, pero la basura y la falta de conciencia siguen siendo un problema."

    l "El río está mejor, pero no podemos bajar la guardia. Esto es solo el comienzo."

    e "Las heridas tardan en sanar. La unión del pueblo es nuestra mayor fuerza."

    v "No puedo cambiar el pasado, pero quiero ser parte de la solución."

    if apoyo_comunidad >= 1:
        n "La comunidad trabaja unida, aunque con desafíos, para proteger el río."
    else:
        n "La denuncia fue un paso, pero falta más compromiso comunitario."

    menu:
        "¿Quieres organizar campañas de educación o establecer diálogo permanente con la fábrica?"
        "Campañas de educación y limpieza":
            n "Se organizan jornadas de limpieza y talleres para cuidar el río."
            jump end_true
        "Diálogo permanente con la fábrica y autoridades":
            n "Se crea un grupo de trabajo para supervisar y mejorar la situación."
            jump end_true

label end_true:
    n "El río muestra signos de vida, pero la lucha por su salud es diaria y colectiva."
    return