import pygame
from Scripts.Interactivos import *
from Scripts.Preguntas import *
import math
import time


class Pantalla:
    Pantalla = 0
    Cargado = 0
    MúsicaDeFondo=0

    '''
    Pantalla 0 = INICIO
    Pantalla 1 = JUEGO
    Pantalla 2 = OPCIONES
    Pantalla 3 = INFORMACIÓN pag1
    Pantalla 4 = INFORMACIÓN pag2
    Pantalla 5 = TUTORIAL
    Pantalla 6 = PREGUNTAS
    Pantalla 7 = RESULTADOS
    
    '''

    Widgets = []
    Texts = []
    Preguntas = []
    Respuestas = []

    FinalPasapalabraResultadosBotones = []

    PreguntaActiva = 0

    Aciertos = 0

    @staticmethod
    def CargaInicio():

        Título = Widget((200, 80), "../Recursos/Imagen/TítuloBase.png")

        BotónJugar = Button((260, 320), (
            "../Recursos/Imagen/BotónJugarBase.png", "../Recursos/Imagen/BotónJugarClickeado.png",
            "../Recursos/Imagen/BotónJugarTocado.png"), 0, 3)
        BotónOpciones = Button((260, 420), (
            "../Recursos/Imagen/BotónOpcionesBase.png", "../Recursos/Imagen/BotónOpcionesClickeado.png",
            "../Recursos/Imagen/BotónOpcionesTocado.png"), 0, 3)

        Pantalla.Widgets = [Título, BotónJugar, BotónOpciones]

        Créditos = Text((400, 580), Text.retro24, "Creado por Lucía Benllochhhhh y Hugo Sánchez", (252, 148, 3))
        Pantalla.Texts = [Créditos]
        Pantalla.Cargado = 0

    @staticmethod
    def CargaPantalla1():
        Pantalla.Cargado = 1

        PestañaJugar = Button((0, 0), (
            "../Recursos/Imagen/PestañaAbiertaJugar.png", "../Recursos/Imagen/PestañaCerradaJugar.png"), 0, 2)
        PestañaInfo = Button((200, 0), (
            "../Recursos/Imagen/PestañaCerradaInformación.png", "../Recursos/Imagen/PestañaAbiertaInformación.png"), 0,
                             2)
        PestañaTutorial = Button((400, 0), (
            "../Recursos/Imagen/PestañaCerradaTutorial.png", "../Recursos/Imagen/PestañaAbiertaTutorial.png"), 0, 2)

        Chat = Widget((0, 500), "../Recursos/Imagen/Chat.png")

        Botón = Button((330, 420), (
            "../Recursos/Imagen/BotónPantalla1.png", "../Recursos/Imagen/BotónPantalla1Clickeado.png",
            "../Recursos/Imagen/BotónPantalla1Tocado.png"), 0, 3)

        Pantalla.Widgets = [PestañaJugar, PestañaInfo, PestañaTutorial, Chat]

        for i in range(16):
            Pantalla.Widgets.append(
                Widget((380 + 160 * math.cos(math.radians(i * 22.5)), 230 + 160 * -math.sin(math.radians(i * 22.5))),
                       "../Recursos/Imagen/BotónAzul.png"))

        Pantalla.Widgets.append(Botón)

        Bienvenida = Text((5, 510), Text.retro24,
                          "Bienvenid@ a MATEXPRESS, para ganar en este juego deberás resolver correctamente las 16",
                          (252, 148, 3))
        Bienvenida2 = Text((5, 538), Text.retro24, "preguntas. Más información en el apartado de tutorial. SUERTE!!",
                           (252, 148, 3))

        Pantalla.Texts = [Bienvenida, Bienvenida2]

    @staticmethod
    def CargaPantalla2():
        Pantalla.Cargado=2

        Fondo=Widget((250,100),"../Recursos/Imagen/FondoOpciones.png")

        BotónSalida=Button((530,80),("../Recursos/Imagen/BotónX.png","../Recursos/Imagen/BotónX.png"),0,2)

        BotónMúsica=Button((260,240),("../Recursos/Imagen/MúsicaActivada.png","../Recursos/Imagen/MúsicaDesactivada.png"),Pantalla.MúsicaDeFondo,2)

        Pantalla.Widgets=[Fondo,BotónSalida,BotónMúsica]

        TOpciones=Text((280,120),Text.arial42,"OPCIONES",(252, 148, 3))
        TMúsica=Text((260,200),Text.arial24,"Música: ",(252, 148, 3))

        Pantalla.Texts=[TOpciones,TMúsica]

    @staticmethod
    def CargaPantalla3():
        Pantalla.Cargado = 3

        PestañaJugar = Button((0, 0), (
            "../Recursos/Imagen/PestañaCerradaJugar.png", "../Recursos/Imagen/PestañaAbiertaJugar.png"), 0, 2)
        PestañaInfo = Button((200, 0), (
            "../Recursos/Imagen/PestañaAbiertaInformación.png", "../Recursos/Imagen/PestañaCerradaInformación.png"), 0,
                             2)
        PestañaTutorial = Button((400, 0), (
            "../Recursos/Imagen/PestañaCerradaTutorial.png", "../Recursos/Imagen/PestañaAbiertaTutorial.png"), 0, 2)

        BotónSiguiente = Button((480, 520), (
            "../Recursos/Imagen/BotónSiguienteBase.png", "../Recursos/Imagen/BotónSiguienteClickeado.png",
            "../Recursos/Imagen/BotónSiguienteTocado.png"), 0, 3)

        Intervalos = Widget((20, 210), "../Recursos/Imagen/Intervalos.png")
        Números = Widget((400, 210), "../Recursos/Imagen/Números.png")

        Pantalla.Widgets = [PestañaJugar, PestañaInfo, PestañaTutorial, Intervalos, Números, BotónSiguiente]

        t1 = Text((20, 80), Text.LM24, "Identidades Notables", (252, 148, 3))
        I1 = Text((40, 110), Text.LM16, "Cuadrado de la suma:    (a+b)^2=a^2+b^2+2ab", (252, 148, 3))
        I2 = Text((40, 130), Text.LM16, "Cuadrado de la diferencia:    (a-b)^2=a^2+b^2-2ab", (252, 148, 3))
        I3 = Text((40, 150), Text.LM16, "Suma por diferencia:    (a+b)(a-b)", (252, 148, 3))

        t2 = Text((20, 180), Text.LM24, "Intervalos", (252, 148, 3))
        t3 = Text((400, 180), Text.LM24, "Números", (252, 148, 3))

        Pantalla.Texts = [t1, I1, I2, I3, t2, t3]

    @staticmethod
    def CargaPantalla4():
        Pantalla.Cargado = 4

        PestañaJugar = Button((0, 0), (
            "../Recursos/Imagen/PestañaCerradaJugar.png", "../Recursos/Imagen/PestañaAbiertaJugar.png"), 0, 2)
        PestañaInfo = Button((200, 0), (
            "../Recursos/Imagen/PestañaAbiertaInformación.png", "../Recursos/Imagen/PestañaCerradaInformación.png"), 0,
                             2)
        PestañaTutorial = Button((400, 0), (
            "../Recursos/Imagen/PestañaCerradaTutorial.png", "../Recursos/Imagen/PestañaAbiertaTutorial.png"), 0, 2)

        BotónAnterior = Button((20, 520), (
            "../Recursos/Imagen/BotónAnteriorBase.png", "../Recursos/Imagen/BotónAnteriorClickeado.png",
            "../Recursos/Imagen/BotónAnteriorTocado.png"), 0, 3)

        Pantalla.Widgets = [PestañaJugar, PestañaInfo, PestañaTutorial, BotónAnterior]

        TPolinomios=Text((320,70),Text.LM32,"Polinomios",(252, 148, 3))

        TSuma=Text((20,130),Text.LM24,"Suma: Se agrupan los términos semejantes",(252, 148, 3))
        TEjemploSuma=Text((20,174),Text.Fpreguntas," (8xY+3x-2)+(4xX-3xY+2x+5)=4xX+5xY+5x+3",(252, 148, 3))
        TEjemploResta = Text((20, 204), Text.Fpreguntas, " (8xY+3x-2)-(4xX-3xY+2x+5)=-4xX+11xY+x-7", (252, 148, 3))

        TMultiplicación = Text((20,244), Text.LM24, "Multiplicación: Se multiplican todos por todos", (252, 148, 3))
        TEjemploMultiplicación=Text((20,288),Text.Fpreguntas," (3x+1)(6xY+2)=18xX+6xY+6x+2",(252, 148, 3))

        TDivisión=Text((20,328),Text.LM24,"División: Se utilizará la regla de ruffini si se da la siguiente forma:",(252, 148, 3))
        TDivisiónEjemplo=Text((20,362),Text.Fpreguntas," P(x):(x-a) // (x-a)=(x--(-a))",(252, 148, 3))

        TRaíces=Text((20,402),Text.LM24,"Raíces de un polinomio:",(252, 148, 3))
        TEjemploRaices=Text((20,446),Text.Fpreguntas," $on raíces todos los números que hacen 0 el polinomio",(252, 148, 3))
        TEjemploRaices2=Text((20,476),Text.Fpreguntas," $olo pueden ser raíces los divisores del término independiente:",(252, 148, 3))


        Pantalla.Texts = [TPolinomios,TSuma,TEjemploSuma,TEjemploResta,TMultiplicación,TEjemploMultiplicación,TDivisión,TDivisiónEjemplo,TRaíces,TEjemploRaices,TEjemploRaices2]

    @staticmethod
    def CargaPantalla5():
        Pantalla.Cargado=5
        PestañaJugar = Button((0, 0), (
            "../Recursos/Imagen/PestañaCerradaJugar.png", "../Recursos/Imagen/PestañaAbiertaJugar.png"), 0, 2)
        PestañaInfo = Button((200, 0), (
            "../Recursos/Imagen/PestañaCerradaInformación.png", "../Recursos/Imagen/PestañaAbiertaInformación.png"), 0,
                             2)
        PestañaTutorial = Button((400, 0), (
            "../Recursos/Imagen/PestañaAbiertaTutorial.png", "../Recursos/Imagen/PestañaCerradaTutorial.png"), 0, 2)

        Pantalla.Widgets=[PestañaJugar,PestañaInfo,PestañaTutorial]

        Título=Text((250,100),Text.arial42,"MATEXPRES",(252, 148, 3))

        P1=Text((20,200),Text.LM24,"En este sencillo juego tu objetivo será resolver las preguntas planteadas",(252, 148, 3))
        P2=Text((20,260),Text.LM24,"La puntuación consistirá en aciertos y fallos según el número de ",(252, 148, 3))
        P22=Text((20,286),Text.LM24,"respuestas correctas",(252, 148, 3))
        P3=Text((20,346),Text.LM24,"No hay límite de tiempo! Tómate las preguntas con calma",(252, 148, 3))
        P4=Text((20,406),Text.LM24,"Mucha suerte y gracias por jugar",(252, 148, 3))

        Pantalla.Texts=[Título,P1,P2,P22,P3,P4]

    @staticmethod
    def CargaPantalla6():
        Pantalla.Cargado = 6
        Pantalla.Respuestas = []
        Pantalla.Aciertos = 0
        Pantalla.PreguntaActiva = 0

        for i in range(4):
            Pantalla.Respuestas.append(0)

        PuntosPasapalabra = []
        for i in range(2):
            for j in range(8):
                PuntosPasapalabra.append(Button((20 + 60 * i, 20 + 75 * j), (
                "../Recursos/Imagen/BotónAzul.png", "../Recursos/Imagen/BotónRojo.png",
                "../Recursos/Imagen/BotónVerde.png"), 0, 3))

        BasePregunta = Widget((160, 80), "../Recursos/Imagen/BasePregunta.png")

        BaseRespuestas = []

        for i in range(4):
            BaseRespuestas.append(Button((180, 220 + 80 * i), (
            "../Recursos/Imagen/FondoRespuestaBase.png", "../Recursos/Imagen/FondoRespuestaTocado.png",
            "../Recursos/Imagen/FondoRespuestaBase.png"), 0, 3))

        for i in range(16):
            Pantalla.Preguntas.append(Pregunta(i))

        Pantalla.Widgets = [PuntosPasapalabra, BasePregunta, BaseRespuestas]

    @staticmethod
    def CargaPantalla7():
        Pantalla.Cargado = 7
        FondoResultados = Widget((100, 100), "../Recursos/Imagen/FondoResultados.png")

        c = 0
        d = 0
        for i in Pantalla.FinalPasapalabraResultadosBotones:
            i.coordinates = (170 + 60 * c, 280 + 60 * d)
            c += 1
            if c == 8:
                d += 1
                c = 0

        BotónVolver = Button((260, 440), (
        "../Recursos/Imagen/BotónVolverBase.png", "../Recursos/Imagen/BotónVolverClickeado.png",
        "../Recursos/Imagen/BotónVolverTocado.png"), 0, 3)

        Pantalla.Widgets = [FondoResultados, Pantalla.FinalPasapalabraResultadosBotones, BotónVolver]

        TResultados = Text((260, 140), Text.arial42, "RESULTADOS", (252, 148, 3))
        TAciertos = Text((240, 220), Text.arial24, "Aciertos: " + str(Pantalla.Aciertos), (252, 148, 3))
        TFallos = Text((460, 220), Text.arial24, "Fallos: " + str(16 - Pantalla.Aciertos), (252, 148, 3))

        Pantalla.Texts = [TResultados, TAciertos, TFallos]

    @staticmethod
    def Inicio():
        c = 0

        for Text in Pantalla.Texts:
            Text.show()

        for Widget in Pantalla.Widgets:
            Widget.show()

            if c > 0:

                if Widget.Clicked():
                    Widget.ChangeState(1)

                    if c == 1:
                        Pantalla.Pantalla = 1
                    else:
                        Pantalla.Pantalla = 2

                elif Widget.Touched():
                    Widget.ChangeState(2)

                elif not Widget.Touched():
                    Widget.ChangeState(0)

            else:
                pass
            c += 1

    @staticmethod
    def Pantalla1():
        c = 0

        for Widget in Pantalla.Widgets:
            Widget.show()

        for Text in Pantalla.Texts:
            Text.show()

        if Pantalla.Widgets[-1].Clicked():
            Pantalla.Widgets[-1].ChangeState(1)
            Pantalla.Pantalla = 6
            time.sleep(0.2)
        elif Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(2)
        elif not Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(0)

        if Pantalla.Widgets[0].Clicked():
            Pantalla.Pantalla = 1
        if Pantalla.Widgets[1].Clicked():
            Pantalla.Pantalla = 3
        if Pantalla.Widgets[2].Clicked():
            Pantalla.Pantalla = 5

        c += 1

    @staticmethod
    def Pantalla2():
        for Widget in Pantalla.Widgets:
            Widget.show()

        for Text in Pantalla.Texts:
            Text.show()

        if Pantalla.Widgets[1].Clicked():
            Pantalla.Pantalla=0

        if Pantalla.Widgets[2].Clicked():

            if Pantalla.MúsicaDeFondo==0:
                Pantalla.Widgets[2].ChangeState(1)
                Pantalla.MúsicaDeFondo=-1
            elif Pantalla.MúsicaDeFondo==1:
                Pantalla.Widgets[2].ChangeState(0)
                Pantalla.MúsicaDeFondo=2

            time.sleep(0.2)

        if Pantalla.MúsicaDeFondo==-1:
            pygame.mixer_music.stop()
            Pantalla.MúsicaDeFondo=1

        elif Pantalla.MúsicaDeFondo==2:
            pygame.mixer_music.play(-1)
            Pantalla.MúsicaDeFondo=0

    @staticmethod
    def Pantalla3():

        for Widget in Pantalla.Widgets:
            Widget.show()

        for Text in Pantalla.Texts:
            Text.show()

        if Pantalla.Widgets[0].Clicked():
            Pantalla.Pantalla = 1
        if Pantalla.Widgets[1].Clicked():
            Pantalla.Pantalla = 3
        if Pantalla.Widgets[2].Clicked():
            Pantalla.Pantalla = 5

        if Pantalla.Widgets[-1].Clicked():
            Pantalla.Widgets[-1].ChangeState(1)
            Pantalla.Pantalla = 4
        elif Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(2)
        elif not Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(0)

    @staticmethod
    def Pantalla4():
        for Widget in Pantalla.Widgets:
            Widget.show()

        for Text in Pantalla.Texts:
            Text.show()

        if Pantalla.Widgets[0].Clicked():
            Pantalla.Pantalla = 1
        if Pantalla.Widgets[1].Clicked():
            Pantalla.Pantalla = 4
        if Pantalla.Widgets[2].Clicked():
            Pantalla.Pantalla = 5

        if Pantalla.Widgets[-1].Clicked():
            Pantalla.Widgets[-1].ChangeState(1)
            Pantalla.Pantalla = 3
        elif Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(2)
        elif not Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(0)

    @staticmethod
    def Pantalla5():
        for Widget in Pantalla.Widgets:
            Widget.show()

        for Text in Pantalla.Texts:
            Text.show()

        if Pantalla.Widgets[0].Clicked():
            Pantalla.Pantalla = 1
        if Pantalla.Widgets[1].Clicked():
            Pantalla.Pantalla = 3
        if Pantalla.Widgets[2].Clicked():
            Pantalla.Pantalla = 5

    @staticmethod
    def Pantalla6():
        Pantalla.Respuestas = []

        for i in range(4):
            Pantalla.Respuestas.append(0)

        c = 0

        for Widget in Pantalla.Widgets:
            if c == 0 or c == 2:
                for i in Widget:
                    i.show()
            else:
                Widget.show()
            c += 1

        if Pantalla.PreguntaActiva == 16:
            time.sleep(0.2)
            Pantalla.FinalPasapalabraResultadosBotones = Pantalla.Widgets[0]
            Pantalla.Pantalla = 7
            Pantalla.PreguntaActiva = 15

        else:
            Pantalla.Preguntas[Pantalla.PreguntaActiva].Preguntar()

        d = 0

        for i in Pantalla.Widgets[2]:

            if i.Clicked():
                i.ChangeState(2)
                Pantalla.Respuestas[d] = 1

                if Pantalla.Respuestas == Pantalla.Preguntas[Pantalla.PreguntaActiva].CódigoRespuestas:
                    Pantalla.Widgets[0][Pantalla.PreguntaActiva].ChangeState(2)
                    Pantalla.Aciertos += 1

                else:
                    Pantalla.Widgets[0][Pantalla.PreguntaActiva].ChangeState(1)

                Pantalla.PreguntaActiva += 1
                time.sleep(0.2)


            elif i.Touched():
                i.ChangeState(1)
            elif not i.Touched():
                i.ChangeState(0)

            d += 1

    @staticmethod
    def Pantalla7():

        c = 0
        for Widget in Pantalla.Widgets:
            if c == 1:
                for i in Widget:
                    i.show()
            else:
                Widget.show()
            c += 1

        for Text in Pantalla.Texts:
            Text.show()

        if Pantalla.Widgets[-1].Clicked():
            Pantalla.Widgets[-1].ChangeState(1)
            Pantalla.Pantalla = 0
            time.sleep(0.2)
        elif Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(2)
        elif not Pantalla.Widgets[-1].Touched():
            Pantalla.Widgets[-1].ChangeState(0)