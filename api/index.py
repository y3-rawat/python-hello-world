key = "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"
from http.server import BaseHTTPRequestHandler
from langchain_groq import ChatGroq

class handler(BaseHTTPRequestHandler):
    def ge(self):
        try:
            
            llm_groq = ChatGroq(groq_api_key=key, model_name="llama3-70b-8192")
            final_title = llm_groq.invoke("hy there how are you").content
            self.wfile.write('Calling from inner function!\n'.encode('utf-8'))
            
            return final_title
        except Exception as e:
            print(f"Error: {e}")
            return "Error in generating response"

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Write initial response parts
        self.wfile.write('Calling from outer function!\n'.encode('utf-8'))

        # Fetch response from ChatGroq
        response = self.ge()
        self.wfile.write(response.encode('utf-8'))
        
        # Additional message
        self.wfile.write('\nHello, world!'.encode('utf-8'))

# Remember to deploy this with a framework that supports WSGI or similar if using Vercel.
