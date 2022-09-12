from playwright.sync_api import sync_playwright
from tkinter import *
import tkinter.messagebox
import requests
import json
from datetime import *


def save_input():
    try:
        dom = txtDom.get("1.0", "end-1c")
        jobId = txtJob.get("1.0", "end-1c")
        token = txtToken.get("1.0", "end-1c")
        urlGetSteps = "https://api.gupy.io/api/v1/jobs/{}/steps".format(jobId)
        admissionDate = datetime.today() + timedelta(days=40)
        accounts = [
            {
                'scene': 'caso01',
                'user': 'testeadmum@tuamaeaquelaursa.com',
                'pass': 'teste123/'
            },
            {
                'scene': 'caso02',
                'user': 'testeadmdois@tuamaeaquelaursa.com',
                'pass': 'teste123/'
            },
            {
                'scene': 'caso03',
                'user': 'testeadmtres@tuamaeaquelaursa.com',
                'pass': 'teste123/'
            },
            {
                'scene': 'caso04',
                'user': 'testeadmquatro@tuamaeaquelaursa.com',
                'pass': 'teste123/'
            }
        ]
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(token)
        }
        findSteps = requests.get(urlGetSteps, {
            "type": "hiring",
            "fields": "id"
        }, headers=headers)
        hiringStep = json.loads(findSteps.content)['results'][0]['id']
        with sync_playwright() as p:
            for accIndex in range(4):
                browser = p.chromium.launch(channel="chrome", headless=False)
                page = browser.new_page()
                url = "https://{}.gupy.io/candidates/jobs/{}/apply".format(dom, jobId)
                page.goto(url)
                page.locator('//*[@id="social-form-acess-button"]').click()
                page.fill('//*[@id="email"]', accounts[accIndex]['user'])
                page.fill('//*[@id="password-input"]', accounts[accIndex]['pass'])
                page.locator('//*[@id="candidates-root"]/div/div[2]/main/div[1]/form/button').click()
                page.wait_for_url(url)
                page.locator('//*[@id="howDidYouHearAboutUs-btn"]').click()
                page.locator('//*[@id="howDidYouHearAboutUs-0"]').click()
                applicationId = page.url.split('/')[5]

                page.locator('//*[@id="isIndicated-off"]/span[1]/span[1]/input').click()
                page.locator('//*[@id="isCompanyEmployee-off"]/span[1]/span[1]/input').click()
                page.locator('//*[@id="additionalInfo"]/div[2]/div/div/div/div[2]/button').click()
                page.locator('//*[@id="candidates-root"]/div/main/div/div/div/div[6]/button|//*['
                             '@id="candidates-root"]/div/main/div/div/div/div[5]/button').click()

                movingAppBody = {"jobId": jobId, "applicationId": applicationId, "currentStepId": hiringStep}
                urlPatchApp = "https://api.gupy.io/api/v1/jobs/{}/applications/{}".format(jobId, applicationId)
                reqPatchApp = requests.patch(url=urlPatchApp,
                                             json=movingAppBody,
                                             headers=headers)
                candidateId = json.loads(reqPatchApp.content)['candidate']['id']

                if candidateId == 24936339:
                    updateHinfoBody = {"jobId": jobId, "applicationId": applicationId,
                                       "hiringType": "employee_admission",
                                       "hiringDate": admissionDate.isoformat()}
                else:
                    updateHinfoBody = {"jobId": jobId, "applicationId": applicationId,
                                       "hiringType": "employee_admission",
                                       "hiringDate": admissionDate.isoformat(), "salary": 1.0,
                                       "salaryCurrencyType": "R$"}
                urlPatchHinfo = "https://api.gupy.io/api/v1/jobs/{}/applications/{}/hiring-information".format(
                    jobId, applicationId)
                reqPatchHinfo = requests.patch(url=urlPatchHinfo,
                                               json=updateHinfoBody,
                                               headers=headers)
                browser.close()

    finally:
        tkinter.messagebox.showinfo('Sucesso!', 'Sucesso')
        window.destroy()


window = Tk()
window.title("Preparação de Admissão - V1")
window.geometry('900x700')
Label(window, text="", height=1, width=40).pack()
Label(window, text="Insira o token").pack(side='top')
txtToken = Text(window, height=1, width=40)
txtToken.pack()
Label(window, text="", height=1, width=40).pack()
Label(window, text="Insira o domínio").pack(side='top')
txtDom = Text(window, height=1, width=40)
txtDom.pack()
Label(window, text="Insira o jobId").pack(side='top')
txtJob = Text(window, height=1, width=40)
txtJob.pack()
Label(window, text="", height=1, width=40).pack()
Label(window, text="", height=1, width=40).pack()
Button(window, text="Enviar", command=save_input).pack()
lblError = Label(window, text="")
lblError.pack()
window.mainloop()
