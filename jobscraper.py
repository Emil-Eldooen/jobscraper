import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib, ssl

# URL for Arbeidsplassen
URL = "URL from Arbeidsplassen.no goes here"

#Get the page
page = requests.get(URL)

#makes page more readable and stores all the page info
prettyPrint = BeautifulSoup(page.content, "html.parser")

#Fetches the main div containing all articles
results = prettyPrint.find("div", class_ = "navds-stack no-focus-outline navds-vstack")

#Finds all the specific articles
jobArticles = results.find_all("article", class_ = "navds-stack navds-hstack")

#Set of companies used to find all the unique companies looking to hire
companiesSet = set()

#Sort through all links and company names in articles
for jobelem in jobArticles:
    jobTitle = jobelem.find("a", href = True).text
    company = jobelem.find("p", class_ = "overflow-wrap-anywhere navds-body-short navds-body-short--medium").text
    
    #Removing any listing with "senior" in the title, change this or expand the words you wish to exclude
    if "senior" in jobTitle.lower():
        continue
    
    #Because Arbeidsplassen only links to the subdomain, the domain itself is not included, hence we need to add it for the link to work anywhere outside of arbeidsplassen.no
    url = "Arbeidsplassen.nav.no" + jobelem.find("a", href = True)["href"]

    #If we find a non-senior position add the company to our set and print out the relevant info
    companiesSet.add(company)
    print("%s\n%s \n%s\n" %(company.strip(), jobTitle.strip(), url))

#The content going into the email
subject = "The subject of the email"
body = "The actual text of the email"

#The email you're sending from and the resipients
sender = "yourmail@gmail.com"
recipients = ["recipient1@mail.com", "recipient2@smtp.com"]

#To get this password ensure 2FA is enabled on the gmail account in question and go to this link: https://security.google.com/settings/security/apppasswords
#Once the password is generated make sure you copy it and then paste it in here and write it down in case you need to refer to it later
password = "Your app password for gmail goes here."

#If you want to automate sending emails you can do this here, only the gmail API is in use so you will need a gmail account:
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['from'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)
