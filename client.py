import google.generativeai as genai

genai.configure(api_key="AIzaSyCsdrQGTzNlE836YFZRXa573ccGKBoDGvE")

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is Programming")
print(response.text)