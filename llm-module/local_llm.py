from google import genai

client = genai.Client(api_key="AIzaSyDvPPIcuEW3pvt7MHgLThBT8pYGEo5NZOg")

def generate_summary(prompt: str):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text



