import ipaddress
import os
import re
import socket
import ssl
import sys
import time
from datetime import datetime

import dns.resolver
import requests
import whois
from cymruwhois import Client
from dotenv import load_dotenv

from src.exception import CustomException
from src.logger import logging
from src.url.url_substrings import URLSubStrings

load_dotenv()
#Calling API's. API keys are stored in .env file
API_KEY = os.getenv("API_KEY")
CX_KEY = os.getenv("CX_KEY")


class url_credentials():
    def __init__(self, url: str):
       #Importing and creating the object of Url Substrings 
       self.url_substrings = URLSubStrings(url)  
       #Assigning the URL from URL substring Constructor to the current class
       self.url = self.url_substrings.url    
       #Getting the URL domain from the URL SubStrings class    
       self.url_domain = self.url_substrings.url_domain()     
       self.url_path_file = self.url_substrings.url_path_file()
       self.url_scheme = self.url_substrings.url_scheme()
       self.url_parameters = self.url_substrings.url_parameters()
       self.url_directory = self.url_substrings.url_domain()
       #to avoid Path/File and Directory are same.
       if self.url_path_file == self.url_directory:
           self.url_directory = None
        
    def time_response(self):
        try:
            response = requests.get(self.url)
            time_response = response.elapsed.total_seconds()
            
            return time_response
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def domain_spf(self):
        try:
            answers = dns.resolver.resolve(self.url_domain, 'TXT')
            for rdata in answers:
                txt_data = rdata.to_text()
                if "v=spf1" in txt_data:
                    return 1
            return 0
       
        except dns.resolver.NXDOMAIN:
            return 0
       
        except dns.resolver.NoAnswer:
            return 0
       
        except dns.resolver.NoNameservers:
            return 0
       
        except Exception as e:
            raise CustomException(e, sys)
        
    def asn_ip(self):
        try:
            c = Client()
            ip = socket.gethostbyname(self.url_domain)
            for r in c.lookupmany([ip]):
               return(r.asn)
           
        except Exception as e:
            raise CustomException(e, sys)
    
    def time_domain_activation_expiration(self):
        try:
            # Initialize variables with default values
            time_domain_activation = -1  # or any default value you prefer
            time_domain_expiration = -1
            
            domain_info = whois.whois(self.url_domain)
            creation_date = domain_info.creation_date
            expiration_date = domain_info.expiration_date

            # Handle None cases first
            if creation_date is None or expiration_date is None:
                return time_domain_activation, time_domain_expiration

            # Handle list cases
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0]

            # Convert string dates to datetime objects
            if isinstance(creation_date, str):
                creation_date = datetime.strptime(creation_date, "%Y-%m-%d")
            if isinstance(expiration_date, str):
                expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

            # Calculate durations only if both dates are valid
            if isinstance(creation_date, datetime) and isinstance(expiration_date, datetime):
                time_domain_activation = (datetime.now() - creation_date).days
                time_domain_expiration = (expiration_date - datetime.now()).days

            return time_domain_activation, time_domain_expiration
            
        except Exception as e:
            CustomException(e, sys)
            logging.error(f"Error in time_domain_activation_expiration: {str(e)}")
            return -1, -1  # Return default values in case of any error
    
    def qty_ip_resolved(self):
        try:
           ips = socket.getaddrinfo(self.url_domain, None)
           return len(ips)
       
        except socket.gaierror:
            logging.info("Error: Could not resolve hostname.")
            return 0
    
        except Exception as e:
           raise CustomException(e, sys)
       
    def qty_nameservers(self):
        try:
            answers = dns.resolver.resolve(self.url_domain, 'NS')
            return len(answers)
        except dns.resolver.NXDOMAIN:
            logging.error("Domain not found.")
            return 0
        except dns.resolver.NoAnswer:
            logging.error("No nameservers found for %s", self.url)
            return 0
        except dns.resolver.NoNameservers:
            logging.error("No nameservers found.")
            return 0
        except Exception as e:
            logging.error("Error: %s", e)
            return 0
    
    def qty_mx_servers(self):
        try:
            answers = dns.resolver.resolve(self.url_domain, 'MX')
            return len(answers)
        except dns.resolver.NXDOMAIN:
            logging.error("Domain not found.")
            return 0
        except dns.resolver.NoAnswer:
            logging.error("No MX servers found for %s", self.url)
            return 0
        except dns.resolver.NoNameservers:
            logging.error("No MX servers found.")
            return 0
        except Exception as e:
            logging.error("Error: %s", e)
            return 0
    
    def ttl_hostname(self):
        try:
            # Resolve the URL to get the TTL value
            answers = dns.resolver.resolve(self.url_domain, 'A')
            # Extract the TTL value from the first answer
            ttl = answers.rrset.ttl
            return ttl
        except dns.resolver.NoAnswer:
            logging.error("No answer found for", self.url)
            return 0
        except dns.resolver.NoNameservers:
            logging.error("Error: No nameservers found.")
            return 0
        except Exception as e:
            logging.error("ttl_hostname Error:", e)
            return 0
        
    def tls_ssl_certificate(self):
        try:
            # Establish a connection to the URL
            context = ssl.create_default_context()
            with socket.create_connection((self.url_domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=self.url_domain) as ssock:
                    # The SSL certificate is considered valid if the connection succeeds
                    return 1
        except Exception as e:
            # If any exception occurs, it means there is no valid SSL certificate
            #logging.error("Error:", e)
            return 0
        
    def qty_redirects(self):
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(self.url, allow_redirects=True)
            
            # Count the number of redirects in the history of the response
            num_redirects = len(response.history)
            return num_redirects
        except Exception as e:
            logging.error("qty_redirects Error:", e)
            return 0
        
    def url_google_index(self):
        try:
            # API endpoint for Google Custom Search JSON API
            api_key =  API_KEY # Replace 'YOUR_API_KEY' with your actual API key
            cx =  CX_KEY # Replace 'YOUR_CX' with your actual search engine ID
            endpoint = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q=site:{self.url}"

            # Send a GET request to the API endpoint
            response = requests.get(endpoint)

            # Check if the response is successful and if the URL is present in the search results
            if response.ok:
                data = response.json()
                items = data.get('items', [])
                for item in items:
                    if item['link'] == self.url:
                        return 1
            return 0
        except Exception as e:
            logging.error("url_google_index Error:", e)
            return 0

    def domain_google_index(self):
        try:
            # To check the the domain index on google we need to pass the Domain alongside Scheme and Oblique. Domain = "Scheme://Domain/" or "Https://youtube.com/ "
            url_scheme_domain = self.url_scheme + "://" + self.url_domain + "/"
            # API endpoint for Google Custom Search JSON API
            api_key =  API_KEY # Replace 'YOUR_API_KEY' with your actual API key
            cx =  CX_KEY # Replace 'YOUR_CX' with your actual search engine ID
            endpoint = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q=site:{url_scheme_domain}"
            
            # Send a GET request to the API endpoint
            response = requests.get(endpoint)

            # Check if the response is successful and if the URL is present in the search results
            if response.ok:
                data = response.json()
                items = data.get('items', [])
                for item in items:
                    if item['link'] == url_scheme_domain:
                        return 1
            return 0
        except Exception as e:
            logging.error("domain_google_index Error:", e)
            return 0
        
    def url_shortened(self):
        try:
           # Get the path component of the URL
            path = self.url_domain
            # Check if the length of the path is shorter than a threshold
            if len(path) <= 10:  # Adjust the threshold as needed
                return 1
            else: 
                return 0
        except Exception as e:
            logging.error("url_shortened error", e)
            return 0
          
    def email_in_url(self):
        try:
            # Regular expression to match an email address
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            
            # Search for email address in the URL
            matches = re.findall(email_regex, self.url)
            
            # If matches are found, return True, otherwise return False
            if matches:
                return 1
            else:
                return 0  
        except Exception as e:
            logging.error("email_in_url error", e)
            return 0 
        
    def domain_in_ip(self):
        try:
            ipaddress.ip_address(self.url_domain)
            return 1
        except Exception:            
            return 0
        
    def server_client_domain(self):
        try:
            domain_lower = self.url_domain.lower()
            if "server" in domain_lower:
                return 1
            elif "client" in domain_lower:
                return 1
            else:
                return 0
        except Exception as e:
            CustomException(e, sys)

          
          
if __name__ == "__main__":
    url = url_credentials("https://twitterserver.com/")
    print(API_KEY)
    print("time_response", url.time_response())
    print("domain_spf", url.domain_spf())
    print("asn_ip", url.asn_ip())
    activation_days, expiration_days = url.time_domain_activation_expiration()
    print("activation_days are :", activation_days)
    print("expiration_days are :", expiration_days)
    print("qty_ip_resolved", url.qty_ip_resolved())
    print("qty_nameservers", url.qty_nameservers())
    print("qty_nameservers", url.qty_mx_servers())
    print("ttl_hostname", url.ttl_hostname())
    print("tls_ssl_certificate", url.tls_ssl_certificate())
    print("qty_redirects", url.qty_redirects())
    print("url_google_index", url.url_google_index())
    print("domain_google_index", url.domain_google_index())
    print("url_shortened", url.url_shortened())
    print("email_in_url", url.email_in_url())
    print("Domain in IP", url.domain_in_ip())
    print("server_client_domain", url.server_client_domain())