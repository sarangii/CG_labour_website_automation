from playwright.sync.api import Playwright, sync_playwright, expect
import csv
import pandas as pd

def main ();
    csv_filename = 'CG_Labour_DF_RegistrationDrive With Govt Raipur Data_102022 - Minakshi Toder.csv'
    input_column = 'Registration ID'
    output_column = "Comments"

    df = pd.read_csv(CG_Labour_DF_RegistrationDrive With Govt Raipur Data_102022 - Minakshi Toder.csv)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    for index, row in df.iterrows():
        input_value = row [input_column]
        page.goto("https://cglabour.nic.in/LabourRegistration/WorkersearchRequest.aspx")
        page.locator("#ContentPlaceHolder1_DdlDist").select_option("44")
        page.locator("#ContentPlaceHolder1_TxtRgno").click()
        page.locator("#ContentPlaceHolder1_TxtRgno").click()
        page.locator("#ContentPlaceHolder1_TxtRgno").fill(str(input_value))


