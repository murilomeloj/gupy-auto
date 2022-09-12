from playwright.sync_api import sync_playwright
from tkinter import *
import tkinter.messagebox
import time


def define_scenario(scene):

    if scene == 'Caso 01 (BR)':  # COM SALÁRIO, SEM RESERVISTA > 25 ANOS, BRASILEIRO, CTPS DIGITAL, BOM JESUS - RS
        return {
            'scene': 'caso01',
            'user': 'testeadmum@tuamaeaquelaursa.com',
            'pass': 'teste123/'
        }
    elif scene == 'Caso 02':  # COM SALÁRIO, COM RESERVISTA > 25 ANOS, ESTRANGEIRO, CTPS
        return {
            'scene': 'caso02',
            'user': 'testeadmdois@tuamaeaquelaursa.com',
            'pass': 'teste123/'
        }
    elif scene == 'Caso 03':  # COM SALÁRIO, BRASILEIRO, CTPS, COM RESERVISTA > 25 ANOS, BOM JESUS - RN
        return {
            'scene': 'caso03',
            'user': 'testeadmtres@tuamaeaquelaursa.com',
            'pass': 'teste123/'
        }
    if scene == 'Caso 04':  # SEM SALÁRIO
        return {
            'scene': 'caso04',
            'user': 'testeadmquatro@tuamaeaquelaursa.com',
            'pass': 'teste123/'
        }


def save_input():
    try:
        dom = txtDom.get("1.0", "end-1c").lower()
        # token = txtToken.get("1.0", "end-1c")
        # vaga = idVaga.get("1.0", "end-1c")
        url = "https://{}.gupy.io/admission/candidates/?invited_source=platform-link".format(dom)
        scene = strScene.get()
        rg = docRg.get()
        aso = docAso.get()
        cns = docCns.get()
        cnh = docCnh.get()
        crnm = docCrnm.get()
        ctps = docCtps.get()
        escolaridade = docEscolaridade.get()
        pis = docPis.get()
        res = docRes.get()
        eleitor = docEleitor.get()
        cpf = docCpf.get()
        reservista = docReservista.get()
        banco = docBanco.get()
        esocial = docEsocial.get()
        foto = docFoto.get()
        testScen = define_scenario(scene)

        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False)
            page = browser.new_page()
            page.goto(url)
            #  início login
            page.locator('//*[@id="social-form-acess-button"]').click()
            page.fill('//*[@id="email"]', testScen['user'])
            page.fill('//*[@id="password-input"]', testScen['pass'])
            page.locator('//*[@id="candidates-root"]/div/div[2]/main/div[1]/form/button').click()
            page.wait_for_url("https://{}.gupy.io/admission/candidates/".format(dom))
            #   fim ‘login’
            #   início aceite dos termos
            # page.locator('//html/body/div/div[3]/div[4]/div/label/span[1]/span[1]/input').click()
            # time.sleep(1)
            # page.locator('//html/body/div/div[3]/div[5]/button').click()
            #   fim aceite dos termos
            page.goto("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            page.locator('//*[@id="root"]/div[3]/div/div[2]/button[1]').click()
            docList = page.url.split('/')[6]
            url = page.url.split('/document-list/')[0]
            page.goto("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if rg == 1:
                page.goto(url + '/document-list/{}/document/3'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[1]/div[2]/input', 'sample.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[2]/div[2]/input', 'sample.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', 'Alan Mathison Turing')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', 'Alan Turing')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                for i in range(2):
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[{}]/div/div[2]/div/button'.format(
                        4 + i)).click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div[2]/div/button').click()
                if testScen['scene'] == 'caso02':
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/div[2]/div/button').click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[8]/div/div[2]/div/button').click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                elif testScen['scene'] == 'caso01':
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Rio Grande')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[8]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Bom Jesus')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                else:
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Rio Grande')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[8]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Bom Jesus')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    #  data de nascimento
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[9]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[83]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                #  fim data de nascimento
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[10]/div/div/input', 'Ethel Sara Stoney')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[11]/div/div/input', 'Julius Mathison Turing')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[12]/div/div/input', '202245949')
                #  data de rg
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[13]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[103]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                #  fim data de rg
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[14]/div/div/input', 'DETRAN')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[15]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if aso == 1:
                page.goto(url + '/document-list/{}/document/35'.format(docList))
                page.set_input_files('//*[@id="root"]/div[3]/div/div[4]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input', 'sample.jpg')
                page.locator('//*[@id="data_exame"]/div/div/div[2]/div').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/button[1]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').first.click()
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if cns == 1:
                page.goto(url + '/document-list/{}/document/33'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input', 'sample.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input', 'sample.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div/div/div/input', '181519167760005')
                time.sleep(1)
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if cnh == 1:
                page.goto(url + '/document-list/{}/document/5'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input', 'sample2.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input', 'sample2.jpg')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', '43515076490')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[103]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                # fim data
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[5]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                # emissão cnh
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[103]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                #  validade cnh
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[133]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                # fim validade cnh
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if crnm == 1:
                page.goto(url + '/document-list/{}/document/37'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[1]/div[2]/input', 'sample.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[2]/div[2]/input', 'sample.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', 'Alan Mathison Turing')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[83]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div[2]/div/button').click()
                if testScen['scene'] == 'caso02':
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                else:
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[5]/div/div/input', '202245949')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div/input', 'CGPI/DUREX/DPF')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/fieldset/div/label[2]').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[8]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[103]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[9]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[133]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[10]/div/fieldset/div/label[2]').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[11]/div/fieldset/div/label[2]').click()
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if ctps == 1:
                page.goto(url + '/document-list/{}/document/8'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[1]/div[2]/input', 'sample.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[2]/div[2]/input', 'sample.jpg')
                if testScen['scene'] == 'caso01':
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', '4559259')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', '5000')
                else:
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', '90031466')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', '021')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div/div[2]/div/input').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[1]/h6').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[2]/div[103]').click()
                page.locator('//html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/div[4]/button').click()
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if escolaridade == 1:
                page.goto(url + '/document-list/{}/document/36'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input', 'sample.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input', 'sample.jpg')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div/div/div[2]/div/button').click()
                page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Mestrado')
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div').click()
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if pis == 1:
                page.goto(url + '/document-list/{}/document/31'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div/div[2]/input', 'sample3.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div/div/div/input', '83602745937')
                time.sleep(1)
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if res == 1:
                page.goto(url + '/document-list/{}/document/2'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div/div[2]/input', 'sample.jpg')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div[2]/div/button').click()
                page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Rua')
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div').click()
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', 'Júlia Kubitschek')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div/div[2]/input', '10')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div/input', 'Muro vermelho e preto')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[5]/div/div/input', 'Centro')
                if testScen['scene'] == 'caso02':
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div[2]/div/button').click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                    for i in range(2):
                        page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[{}]/div/div[2]/div/button'.
                                     format(i + 7)).click()
                        page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[9]/div/div[1]/input', '95290970')
                elif testScen['scene'] == 'caso01':
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div[2]/div/button').click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Rio Grande')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[8]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Bom Jesus')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[9]/div/div[1]/input', '95290970')
                else:
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div[2]/div/button').click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[7]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Rio Grande')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[8]/div/div[2]/div/button').click()
                    page.fill('//html/body/div[2]/div[2]/div/div[1]/div/div/input', 'Bom Jesus')
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[9]/div/div[1]/input', '59270970')
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if eleitor == 1:
                page.goto(url + '/document-list/{}/document/6'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[1]/div[2]/input', 'sample.jpg')
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div[2]/div[2]/input', 'sample.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', '252173442496')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', '001')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div/input', '001')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div[2]/div/button').click()
                page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if cpf == 1:
                page.goto(url + '/document-list/{}/document/4'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[2]/div/div/div/div[2]/input', 'sample.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div/div/div/input', '22599783046')
                time.sleep(1)
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if reservista == 1:
                page.goto(url + '/document-list/{}/document/7'.format(docList))
                if testScen['scene'] == 'caso01':
                    page.locator('//html/body/div/div[3]/div/div[2]/label/span[1]/span[1]/input').click()
                    page.locator('//html/body/div/div[3]/div/div[3]/button').click()
                else:
                    page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[1]/div[2]/input|'
                                         '//html/body/div/div[3]/div/div[2]/div/div/div[1]/div[2]/input', 'sample.jpg')
                    page.set_input_files('//html/body/div/div[3]/div/div[3]/div/div/div[2]/div[2]/input|'
                                         '//html/body/div/div[3]/div/div[2]/div/div/div[2]/div[2]/input', 'sample.jpg')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', 'Dispensado')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', '101010101010')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div/input', '3ª')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div/input', '1ª RM')
                    page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[5]/div/div/input', 'Ministério da Defesa')
                    page.locator('//html/body/div/div[3]/div/form/div[1]/div/div[6]/div/div[2]/div/button').click()
                    page.locator('//html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]').click()
                    page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url(
                        "https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if banco == 1:
                page.goto(url + '/document-list/{}/document/32'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input', 'sample4.jpg')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[1]/div/div/input', 'Bradesco')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[2]/div/div/input', '1986')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[3]/div/div/input', '1865052')
                page.fill('//html/body/div/div[3]/div/form/div[1]/div/div[4]/div/div/input', '5')
                time.sleep(1)
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if esocial == 1:
                page.goto(url + '/document-list/{}/document/12'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input', 'sample.jpg')
                page.locator('//html/body/div/div[3]/div/form/div[1]/div/div/div/fieldset/div/label[1]').click()
                time.sleep(1)
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            if foto == 1:
                page.goto(url + '/document-list/{}/document/34'.format(docList))
                page.set_input_files('//html/body/div/div[3]/div/div[4]/div/div/div/div[2]/input|'
                                     '//html/body/div/div[3]/div/div[3]/div/div/div/div[2]/input', 'sample.jpg')
                page.locator('//html/body/div/div[3]/div/form/div[2]/button').click()
                page.wait_for_url("https://{}.gupy.io/admission/candidates/workflow-step/SEND_DOCUMENTS".format(dom))
            browser.close()

    finally:
        tkinter.messagebox.showinfo('Sucesso!', 'Sucesso')
        window.destroy()


window = Tk()
docTermos = IntVar()
docRg = IntVar()
docAso = IntVar()
docCns = IntVar()
docCnh = IntVar()
docCrnm = IntVar()
docCtps = IntVar()
docEscolaridade = IntVar()
docPis = IntVar()
docRes = IntVar()
docEleitor = IntVar()
docCpf = IntVar()
docReservista = IntVar()
docBanco = IntVar()
docEsocial = IntVar()
docFoto = IntVar()
strScene = StringVar()
strScene.set('Caso 01 (BR)')

window.title("Teste de Admissão - V1")
window.geometry('900x700')
Label(window, text="", height=1, width=40).pack()
Label(window, text="Insira o domínio").pack(side='top')
txtDom = Text(window, height=1, width=40)
txtDom.pack()
Label(window, text="Selecione o cenário de teste").pack(side='top')
OptionMenu(window, strScene, "Caso 01 (BR)", "Caso 02", "Caso 03", "Caso 04").pack()
Label(window, text="", height=1, width=40).pack()
Label(window, text="Lista de documentos").pack()
Checkbutton(window, text="RG", onvalue=1, offvalue=0, variable=docRg).pack()
Checkbutton(window, text="ASO", onvalue=1, offvalue=0, variable=docAso).pack()
Checkbutton(window, text="CNS", onvalue=1, offvalue=0, variable=docCns).pack()
Checkbutton(window, text="CNH", onvalue=1, offvalue=0, variable=docCnh).pack()
Checkbutton(window, text="CRNM", onvalue=1, offvalue=0, variable=docCrnm).pack()
Checkbutton(window, text="CTPS", onvalue=1, offvalue=0, variable=docCtps).pack()
Checkbutton(window, text="ESCOLARIDADE", onvalue=1, offvalue=0, variable=docEscolaridade).pack()
Checkbutton(window, text="PIS", onvalue=1, offvalue=0, variable=docPis).pack()
Checkbutton(window, text="RESIDÊNCIA", onvalue=1, offvalue=0, variable=docRes).pack()
Checkbutton(window, text="ELEITOR", onvalue=1, offvalue=0, variable=docEleitor).pack()
Checkbutton(window, text="CPF", onvalue=1, offvalue=0, variable=docCpf).pack()
Checkbutton(window, text="RESERVISTA", onvalue=1, offvalue=0, variable=docReservista).pack()
Checkbutton(window, text="DADOS BANCÁRIOS", onvalue=1, offvalue=0, variable=docBanco).pack()
Checkbutton(window, text="ESOCIAL", onvalue=1, offvalue=0, variable=docEsocial).pack()
Checkbutton(window, text="FOTO", onvalue=1, offvalue=0, variable=docFoto).pack()


Label(window, text="", height=1, width=40).pack()
Button(window, text="Iniciar", command=save_input).pack()
lblError = Label(window, text="")
lblError.pack()
window.mainloop()
