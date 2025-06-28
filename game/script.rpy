
define s = Character("Jeremy")
define m = Character("Martín")
define d = Character("Dailyn")

image fondo_intro = "helicoptero6.jpg"
image fondo1 = "cabina4.png"
image fondo2 = "inicio-lancha2.jpg"
image fondo3 = "imagen-desarrollo2.jpg"
image fondo4 = "desarrollo-3.jpg"
image fondo5 = "zona-industrial2.jpg"
image fondo6 = "agua-negra2.jpg"

image jeremy = "jeremy.png"
image martin = "martin.png"
image dailyn = "dailyn2.png"


label start:

    play music "uncharted.mp3" fadein 2.5
    scene fondo_intro with fade
    "Presiona espacio para continuar"
    stop music fadeout 1.0

    jump marco_polo

label marco_polo:
    play music "uncharted2.mp3" fadein 1.0
    scene black with fade
    show text "“Nunca sabremos el valor del agua,\nhasta que el pozo esté seco.”\n- Benjamin Franklin\n17 de abril 1790" at truecenter with Dissolve(2.0)
    $ renpy.pause(8.0)
    hide text with Dissolve(1.5)
    stop music fadeout 1.0

    jump helicoptero

label helicoptero:
    scene black
    play sound "helicoptero.mp3"
    $ renpy.pause(8.0)
    stop sound

    jump juego_principal

label juego_principal:

    
    $ confianza_comunidad = 0
    $ accion_urgente = 0
    $ errores = 0

    
    scene fondo1 with dissolve
    show jeremy at left
    s "El informe es peor de lo esperado. Químicos ilegales están en el agua."
    menu:
        "¿Qué quieres hacer?"
        "Exponer públicamente a la empresa":
            $ confianza_comunidad += 30
        "Investigar en secreto primero":
            $ accion_urgente += 1

    
    scene fondo2 with dissolve
    show martin at left
    m "Un niño enfermó por beber del río. No hay tiempo."
    menu:
        "Contener químicamente la zona":
            $ accion_urgente += 1
        "Llamar a los medios":
            $ confianza_comunidad += 20

    
    hide martin
    show dailyn at left
    d "La comunidad culpa al equipo por no actuar antes."
    menu:
        "Asumir responsabilidad":
            $ confianza_comunidad += 30
        "Culpar al gobierno":
            $ errores += 1

    
    scene fondo4 with dissolve
    show jeremy at left
    s "Los peces están muriendo río abajo. ¿Actuamos sin permiso?"
    menu:
        "Usar drones y lanzar neutralizante":
            $ accion_urgente += 1
        "Esperar al consejo ambiental":
            $ errores += 1

    
    scene fondo5 with dissolve
    show martin at left
    m "La empresa ha cerrado el acceso al río. Dicen que es una 'zona de seguridad'."
    menu:
        "Entrar a escondidas con ayuda local":
            $ confianza_comunidad += 20
            $ accion_urgente += 1
        "Esperar una orden judicial":
            $ errores += 1

    
    scene fondo6 with dissolve
    show dailyn at left
    d "El agua negra llegó al pueblo. Los niños están en peligro."
    menu:
        "Evacuar por cuenta propia":
            $ accion_urgente += 1
        "Buscar ayuda del gobierno":
            $ errores += 1

    
    scene fondo1 with dissolve
    show jeremy at left
    s "Hicimos lo que pudimos... pero no sé si fue suficiente."

    if errores >= 3:
        "El desastre se expandió. La comunidad te culpa. Hay muertes y desplazamiento forzado."
    elif accion_urgente >= 3 and confianza_comunidad >= 50:
        "Actuaste con firmeza y humanidad. El río fue restaurado, pero solo tras un doloroso sacrificio."
    else:
        "Salvaste a parte del pueblo. Pero hubo pérdidas irreparables, y la flora local desapareció."

    return