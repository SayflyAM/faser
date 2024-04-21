import streamlit as st
import google.generativeai as genai

# Streamlit app title
st.title("Chatbot with Streamlit")

# Configure generative AI
genai.configure(api_key="AIzaSyDOYIv0sDULoFLFDj88VklpODGlqH-UdMs")
model = genai.GenerativeModel('gemini-pro')

# Function to handle user input and generate response
def generate_response(user_input):
    # Append the welcome message to the user's input
    input_with_message = user_input + "أهلاً بك في بوت تفسير الأحلام! هل حلمت بشيء محير وترغب في فهم معناه؟ أو ربما تريد معرفة ماذا يعني حلمك الأخير؟ اكتب لي الآن حلمك، وسأعمل جاهدًا لتقديم تفسير دقيق ومعمق لهذا الحلم. دعني أساعدك في فهم عالم الأحلام ومعانيها"
    response = model.generate_content(input_with_message)
    return response.text

# Main Streamlit app
def main():
    # Streamlit UI components
    user_input = st.text_input("Enter your dream:")
    if st.button("Send"):
        response = generate_response(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
