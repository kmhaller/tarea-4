import requests, csv
import xml.etree.ElementTree as et
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# location given here
#location = "delhi technological university"
# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address':location}
# sending get request and saving the response as response object
def generar_df(URL):
    response = requests.get(url = URL).content
    # extracting data in json format
    #data = response.json()
    print('>> XML_DF:', len(response))

    #tree = et.parse(response.text)
    #root = tree.getroot()

    #root = et.fromstring(response) #element tree
    root = et.XML(response)
    df_cols = ["GHO","COUNTRY","SEX","YEAR","GHECAUSES","AGEGROUP","Display","Numeric","Low","High"]
    xml_list = []
    for child in root:
        xml_dict = {"GHO":0,"COUNTRY":0,"SEX":0,"YEAR":0,"GHECAUSES":0,"AGEGROUP":0,"Display":0,"Numeric":0,"Low":0,"High":0}
        #xml_dict['Data'] = child.attrib[""]
        for subchild in child:
            filtro = False
            if (subchild.tag)== "GHO":
                if "Number of deaths" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Number of infant deaths" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Number of under-five deaths" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimates of number of homicides" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Crude suicide rates (per 100 000 population)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Mortality rate attributed to unintentional poisoning (per 100 000 population)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Number of deaths attributed to non-communicable diseases, by type of disease and sex" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimated road traffic death rate (per 100 000 population)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimated number of road traffic deaths" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Mean BMI" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)" == subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimate of daily cigarette smoking prevalence (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimate of daily tobacco smoking prevalence (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimate of current cigarette smoking prevalence (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Estimate of current tobacco smoking prevalence (%)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Mean systolic blood pressure (crude estimate)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Mean fasting blood glucose (mmol/l) (crude estimate)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                elif "Mean Total Cholesterol (crude estimate)" in subchild.text:
                    xml_dict["GHO"] = subchild.text
                else:
                    filtro = True

            if filtro == False:
                if (subchild.tag)== "COUNTRY":
                    xml_dict["COUNTRY"] = subchild.text
                elif (subchild.tag)== "SEX":
                    xml_dict["SEX"] = subchild.text
                elif (subchild.tag)== "YEAR":
                    xml_dict["YEAR"] = subchild.text
                elif (subchild.tag)== "GHECAUSES":
                    xml_dict["GHECAUSES"] = subchild.text
                elif (subchild.tag)== "AGEGROUP":
                    xml_dict["AGEGROUP"] = subchild.text
                elif (subchild.tag)== "Display":
                    xml_dict["Display"] = subchild.text
                elif (subchild.tag)== "Numeric":
                    xml_dict["Numeric"] = subchild.text
                elif (subchild.tag)== "Low":
                    xml_dict["Low"] = subchild.text
                elif (subchild.tag)== "High":
                    xml_dict["High"] = subchild.text
        if xml_dict["GHO"] != 0:
            xml_list.append(xml_dict)
    return xml_list
#xml_df = pd.DataFrame(xml_list)
#print(xml_df.to_string())

cod_pais = ["CHL","DEU","USA","NLD","BGD","CRI"]

URL = f"http://tarea-4.2021-1.tallerdeintegracion.cl/gho_CHL.xml"
# generando xml
lista = generar_df(URL)
#df = generar_df(URL)

for codigo in cod_pais[1:]:
    
    URL = f"http://tarea-4.2021-1.tallerdeintegracion.cl/gho_{codigo}.xml"
    # generando xml
    lista_nueva = generar_df(URL)
    for element in lista_nueva:
        lista.append(element)

df = pd.DataFrame(lista)
print(df.to_string())
# acces google sheet
gc = gspread.service_account(filename='taller-tarea-4-info-desde-api-22ee764b8cdb.json')
sh = gc.open_by_key('1UQNEc8kbnNCSXLiTTC8IeR85H9RBX-isD3_LLqQMwHI')
worksheet = sh.get_worksheet(0) #-> 0 - first sheet, 1 - second sheet etc.

# append data to sheet
worksheet.clear()
set_with_dataframe(worksheet, df) # -> this exports df to google sheets