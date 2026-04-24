import requests

url = "https://windbornesystems.com/career_applications.json"

data = {
  "career_application": {
    "name": "Abhishek Patil",
    "email": "abhipatil3515@gmail.com",
    "role": "Sensors Intern",
    "notes": "I would choose Ladakh, India for the next balloon launch site because of its high altitude, low humidity, and unique atmospheric conditions. It provides an ideal environment to test sensor robustness, calibration drift, and performance in data-sparse regions.",
    "submission_url": "https://github.com/Abhipatilap09/windborne-sensors-intern",
    "resume_url": "https://drive.google.com/file/d/1VwQZnez2cj3dvY2fh6-PjFuyCBK2Z2FD/view?usp=sharing"
  }
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:", response.text)
