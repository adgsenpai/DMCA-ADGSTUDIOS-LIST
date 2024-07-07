import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Step 1: Read Existing ./static/db/list.txt
with open('./static/db/list.txt', 'r') as file:
    existing_urls = file.readlines()
existing_urls = [url.strip() for url in existing_urls]

# Step 2: Read New URLs from filtered_urls.csv
new_urls_df = pd.read_csv('filtered_urls.csv')
new_urls = new_urls_df['URL'].tolist()

# Must remove https://
new_urls = [url.replace('https://', '') for url in new_urls]

# remove if the url is anime.adgstudios.co.za/
new_urls = [url for url in new_urls if url != 'anime.adgstudios.co.za/']

# Step 3: Check for Duplicates and Add Unique URLs
unique_new_urls = [url for url in new_urls if url not in existing_urls]

# Step 4: Write Updated List Back to ./static/db/list.txt
with open('./static/db/list.txt', 'a') as file:
    file.write("\n")
    for url in unique_new_urls:
        file.write(f"{url}\n")

# Don't leave empty line at the end of the file
with open('./static/db/list.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = list(filter(None, lines))

with open('./static/db/list.txt', 'w') as file:
    for line in lines:
        if line == lines[-1]:
            file.write(f"{line}")
        else:
            file.write(f"{line}\n")

# Step 5: Generate and Send an Email Report
# Prepare email content
subject = "DMCA Links Update"
body = f"The following new URLs have been added to the DMCA list:\n\n" + "\n".join(unique_new_urls)
sender_email = "adg@adgstudios.co.za"
receiver_email = "adg@adgstudios.co.za"
password = os.getenv("EMAIL_PASSWORD")

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    server = smtplib.SMTP('smtpout.secureserver.net', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")