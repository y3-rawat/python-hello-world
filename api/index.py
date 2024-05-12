from http.server import BaseHTTPRequestHandler
from langchain_groq import ChatGroq

class handler(BaseHTTPRequestHandler):
    def ge(self):
        key = "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"
        llm_groq = ChatGroq(groq_api_key=key, model_name="llama3-70b-8192")
        final_title = llm_groq.invoke("hy there how are you").content
        
        # Corrected method to include self and return a string
        return final_title

    def do_GET(self):
        # Send HTTP status 200 (OK)
        self.send_response(200)
        # Set the Content-type header
        self.send_header('Content-type', 'text/plain')
        # End headers (important in HTTP responses)
        self.end_headers()
        
        # Writing response body
        # Corrected method call to self.ge()
        response = self.ge()
        self.wfile.write(response.encode('utf-8'))  # Encode response to UTF-8
        self.wfile.write('\nHello, world!'.encode('utf-8'))  # Additional message

# This handler can be used with a WSGI server to deploy to Vercel
