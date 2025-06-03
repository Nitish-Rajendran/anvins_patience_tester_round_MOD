# 📞 WhatsApp Group Monitor with Twilio Voice Call Alerts

This Python script monitors a specified WhatsApp group using **Selenium** and automatically triggers a **Twilio voice call** when a new message appears. It's perfect for critical alerting systems where WhatsApp activity requires instant attention.

---

## 🚀 Features

- 🔍 Real-time monitoring of a WhatsApp group
- 📞 Automated phone call when a new message is detected
- 🔒 Environment-based secret management using `.env`
- 🧰 Uses `selenium`, `twilio`, and `webdriver-manager` for portability and ease

---

## 🛠 Requirements

- Python 3.7+
- Google Chrome browser installed
- Twilio account with a verified phone number

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nitish-Rajendran/anvins_patience_tester_round_MOD
cd yourrepo
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
requirements.txt should contain:
```bash
selenium
twilio
python-dotenv
webdriver-manager
```

### 3. Configure Environment Variables
Create a .env file in the project root with the following:

```bash
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890
YOUR_PHONE_NUMBER=+0987654321
```

⚠️ Important: Never commit your .env file to a public repository.

### 4. Update the WhatsApp Group Name
In auto.py, set your group name:

```bash
GROUP_NAME = "Your WhatsApp Group Name"
Ensure it matches the name exactly as it appears in WhatsApp Web.
```

---

## Running the Script

Execute the following command in Terminal by running it as Administrator
```bash
python auto.py
```

You’ll be prompted to scan the WhatsApp QR code if not previously authenticated. The script waits for new messages in the specified group. On detecting a new message, it triggers a Twilio voice call to your configured number.

---

## How It Works
- Selenium automates WhatsApp Web.
- It waits for new messages in the target group chat.
- On a new message, it uses the Twilio API to call your phone number.
- Voice message is the default Twilio XML demo (http://demo.twilio.com/docs/voice.xml).
- Twilio Connection Test
- Before starting the monitor, the script initiates a test call to confirm that Twilio credentials are working. If the credentials are invalid, the script exits gracefully with an error.

---

## Notes
- You can customize the voice call message by hosting your own TwiML XML.
- Twilio trial accounts require verified phone numbers (no calls to unverified numbers).

---

## Security Tips
- Avoid hardcoding credentials in your script.
- Use .env + python-dotenv for loading secrets.
- Set up a .gitignore to exclude your .env file:

```bash
.env
```

---

## License
This project is open-source and available under the MIT License.

---

## Support
If you encounter issues or have feature requests, feel free to open an issue.



half of this is okay but include ``` or ## or - wherever included sso the readme looks good and response as a .txt file
