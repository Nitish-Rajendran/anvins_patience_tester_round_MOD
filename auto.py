import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from twilio.rest import Client
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
from dotenv import load_dotenv
load_dotenv()

# Configuration Parameters
GROUP_NAME = ""  # Replace with your WhatsApp group name
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")


# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def make_phone_call():
    try:
        call = twilio_client.calls.create(
            to=YOUR_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url='http://demo.twilio.com/docs/voice.xml'  # Default Twilio voice message
        )
        print(f"Call initiated: {call.sid}")
    except Exception as e:
        print(f"Error making call: {e}")

def monitor_whatsapp():
    # Set up Chrome options
    # In the monitor_whatsapp function, modify the chrome_options setup:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=./chrome_profile")
    chrome_options.add_argument(f"--remote-debugging-port={random.randint(9222,9999)}")  # Random port
    chrome_options.add_argument("--no-sandbox")  # Reduce restrictions
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Disable automation flag
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # Keep the rest of your driver initialization the same
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.get("https://web.whatsapp.com")
    
    try:
        # Wait for QR code scan and load
        print("Please scan the QR code if prompted...")
        group_xpath = f'//span[@title="{GROUP_NAME}"]'
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, group_xpath))
        )
        
        # Click on the group
        group = driver.find_element(By.XPATH, group_xpath)
        group.click()
        
        # Replace the message count logic with:
        last_message = None
        
        while True:
            try:
                # Wait for new messages
                new_messages = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, "div[role='row'] div[data-pre-plain-text]")
                    )
                )
                
                if new_messages:
                    latest_message = new_messages[-1]
                    
                    if latest_message != last_message:
                        print("New message detected! Making phone call...")
                        make_phone_call()
                        last_message = latest_message
                        
                time.sleep(2)
                
            except TimeoutException:
                print("No new messages detected in this check")
                continue
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

# Add this before monitor_whatsapp() call:
if __name__ == "__main__":
    # Verify Twilio credentials first
    try:
        test_call = twilio_client.calls.create(
            to=YOUR_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml",
            status_callback_event="initiated",
            status_callback="https://twilio.com"
        )
        print(f"Twilio test call initiated: {test_call.sid}")
    except Exception as e:
        print(f"Twilio connection failed: {e}")
        exit()
    
    monitor_whatsapp()