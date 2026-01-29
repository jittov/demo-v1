import google.generativeai as genai

# ⚠️ REPLACE THIS WITH YOUR NEW KEY - never share it!
API_KEY = "AIzaSyBbMg97b5sHJwlQeZwsJoSbb1bS2NrBqKE"

def test_gemini_basic():
    """Basic test of Gemini API"""
    try:
        # Configure the API
        genai.configure(api_key=API_KEY)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Test query
        response = model.generate_content("Explain quantum computing in one sentence")
        
        print("✅ API Test Successful!")
        print(f"Response: {response.text}")
        print(f"Response length: {len(response.text)} characters")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_gemini_basic()