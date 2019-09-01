import pyautogui, time, pymsgbox, clipboard, datetime

#PASSO 1
def abrirNavegador():
    #ABRINDO O NAVEGADOR
    pyautogui.moveTo(266,747)
    pyautogui.click()
    time.sleep(1)
    #print('Abrir Navegador')


def abrirPlanilha():
    #ABRINDO PLANILHA
    adicionarAba()
    pyautogui.typewrite('url planilha do Google Planilhas')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.moveTo(145, 235)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(265, 385)
    time.sleep(0.5)
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/filtroPlanilha.png')
    time.sleep(0.5)
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/okPlanilha.png')
    time.sleep(0.3)
    pyautogui.moveTo(115, 260)
    time.sleep(0.2)
    pyautogui.click()
    from datetime import date, timedelta
    dataOntem = date.today() - timedelta(1)
    time.sleep(0.2)
    pyautogui.typewrite(str(dataOntem))
    pyautogui.press('enter')
    time.sleep(0.5)
    vaiSat()


#PASSO 3
def adicionarAba():
    pyautogui.moveTo('C:/Users/Usr/Desktop/ProgramaSat/adicionarAba.png')
    pyautogui.click()
    pyautogui.click(460,50)
    time.sleep(0.5)

#PASSO 2
def abrirSat():
    #ACESSANDO O SISTEMA
    #PASSO 3
    adicionarAba()
    pyautogui.typewrite('www.sitederastreamento.com.br')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.moveTo(1115, 190)
    pyautogui.click()
    time.sleep(2)
    #print('Abrir Sat')
    loginSat()

def entarSat():
    print('Clicar Enter')
    pyautogui.moveTo(760, 360)
    pyautogui.click()


def loginSat():
    pyautogui.moveTo(651, 263)
    pyautogui.doubleClick()
    pyautogui.press('del')
    pyautogui.typewrite('usuario', interval = 0.15)
    pyautogui.press('tab')
    pyautogui.moveTo(628, 306)
    pyautogui.doubleClick()
    pyautogui.press('del')
    pyautogui.typewrite('senha', interval = 0.15)
    pyautogui.press('tab')
    pyautogui.moveTo(760, 360)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/salvarSenha.png')
    time.sleep(2)
    print('Login Sat')

def navegarSistema():
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/ultimosregistros.png')
    time.sleep(2)
    pyautogui.click(119, 269)
    time.sleep(1)
    pyautogui.press(['backspace', 'backspace'])
    dayInt = datetime.datetime.now().day - 1
    dayString = str(dayInt)
    pyautogui.typewrite(dayString)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/lupa.png')
    time.sleep(1)
    pyautogui.click(313, 298)
    time.sleep(1)

def buscaVWBXXXX():
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/Placa1.png')
    time.sleep(1)
    veiculo = 'Placa1'
    return veiculo


def buscaDXBXXXX():
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/Placa2.png')
    time.sleep(1)
    veiculo = 'Placa2'
    return veiculo



def buscaSNFXXXX():
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/Placa3.png')
    time.sleep(1)
    veiculo = 'Placa3'
    return veiculo


def buscaQUFXXXX():
    pyautogui.click('C:/Users/Usr/Desktop/ProgramaSat/Placa4.png')
    time.sleep(1)
    veiculo = 'Placa4'
    return veiculo


def busca():
    pyautogui.moveTo(230, 380)
    pyautogui.click(pyautogui.click(button='left', clicks=2, interval=0.25))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    colar = clipboard.paste()
    i = 1
    while i > 0:
        if colar.find('Ignição ligada') > -1 or colar.find('Periódica') > -1:

            pyautogui.moveTo(485, 380)
            pyautogui.click(pyautogui.click(button='left', clicks=2, interval=0.25))
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            colar = clipboard.paste()
            horaDestinoFinal = colar[11:16]

            pyautogui.moveTo(1215, 380)
            pyautogui.click(pyautogui.click(button='left', clicks=2, interval=0.25))
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            colar = clipboard.paste()

            lista = colar.split(' ')
            cidade = len(colar.split(' ')) - 5

            destinoFinal = lista[cidade]
            time.sleep(1)
            vaiPlanilha()

            time.sleep(1)
            pyautogui.moveTo(285, 260)
            pyautogui.click()
            pyautogui.typewrite(destinoFinal)
            time.sleep(0.5)
            pyautogui.moveTo(465, 260)
            pyautogui.click()
            pyautogui.typewrite(horaDestinoFinal)

            #VOLTA PARA O SAT
            vaiSat()
            i = -1
        else:
            pyautogui.scroll(-385)
            pyautogui.click(pyautogui.click(button='left', clicks=2, interval=0.25))
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            colar = clipboard.paste()

def vaiPlanilha(caminhao):
    pyautogui.moveTo('C:/Users/Usr/Desktop/ProgramaSat/planilhaHoras.png')
    pyautogui.click()

    if caminhao == 'Placa1':
        print('Deu certo! ')
    elif caminhao == 'Placa2':
        print('Deu certo! ')
    elif caminhao == 'Placa3':
        print('Deu certo! ')
    else:
        print('Deu certo! Placa4')
def vaiSat():
    pyautogui.moveTo('C:/Users/Usr/Desktop/ProgramaSat/superSat.png')
    pyautogui.click()

