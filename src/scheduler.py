from datetime import datetime
import schedule
import time
from email_sender import send_email
from config import RECIPIENTS

def job():
    subject = "Scheduled Email: "
    # Determine the template based on the current time
    # You can modify the time ranges as per your requirements
    current_time = datetime.now().time()
    if current_time >= datetime.strptime("06:00", "%H:%M").time() and current_time < datetime.strptime("12:00", "%H:%M").time():
        template = 'src/templates/good_morning.html'
        subject += "Good Morning"
        
    elif current_time >= datetime.strptime("12:00", "%H:%M").time() and current_time < datetime.strptime("17:00", "%H:%M").time():
        template = 'src/templates/good_afternoon.html'
        subject += "Good Afternoon"
        
    elif current_time >= datetime.strptime("17:00", "%H:%M").time() and current_time < datetime.strptime("18:00", "%H:%M").time():
        template = 'src/templates/good_noon.html'
        subject += "Good Noon"
        
    elif current_time >= datetime.strptime("18:00", "%H:%M").time() and current_time < datetime.strptime("21:00", "%H:%M").time():
        template = 'src/templates/good_evening.html'
        subject += "Good Evening"
        
    else:
        template = 'src/templates/good_night.html'
        subject += "Good Night"
    
    # Load the HTML content from the template file
    with open(template, 'r') as file:
        html_content = file.read()
    
    # Send email using Gmail SMTP
    send_email(subject, RECIPIENTS, html_content)
    print(f"Email sent with template: {template} at {current_time}")

# Schedule the job to run at specific times
schedule.every().day.at("06:00").do(job)
schedule.every().day.at("14:03").do(job)
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("21:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)