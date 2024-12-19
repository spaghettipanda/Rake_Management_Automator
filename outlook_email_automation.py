# %%
# https://itsec.media/post/python-send-outlook-email/

import win32com.client
from win32com.client import Dispatch, constants
from datetime import date as dt
    
# Generate email - All elements are hardcoded except csv table data and signature sign off
def generate_email(cycle_points, car_counts):
    const=win32com.client.constants
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    date = dt.today().strftime("%d-%B-%Y")
    newMail.Subject = f"Data Corrections Required for {date}"
    newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
    newMail.GetInspector
    index = newMail.HTMLbody.find('>', newMail.HTMLbody.find('<p')) 

    newMail.HTMLBody = newMail.HTMLbody[:index + 1] + (f'Hi HLO/MTM team,<br><br>Please assist with the data corrections for the following rakes:<br><br><span style=\"text-decoration: underline;\"><strong>Cycle Point Events</strong></span><br>{cycle_points}<br><span style=\"text-decoration: underline;\"><strong>Car Count Events</strong></span><br>{car_counts}<br>Thank you in advance,') + newMail.HTMLbody[index + 1:]
    newMail.To = 'dl-ior-per-ironperiopshubscheduling@bhp.com; dl-tech-railhistorian-productteam@bhp.com; DL-IOR-Perth-AS-MTSupport@bhp.com'
    newMail.CC = 'dl-tech-minaus-run-troc-otproductionapplications@bhp.com; shaily.singh2@bhp.com; sathish.vailaya@bhp.com; iops_productionaccounting@bhp.com'

    # Display email as a pop up instead of sending immediately
    newMail.display()
