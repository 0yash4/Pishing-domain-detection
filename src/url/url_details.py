import sys
from dataclasses import dataclass
from urllib.parse import parse_qs, urlparse

from src.exception import CustomException
from src.logger import logging
from src.url.url_substrings import URLSubStrings


@dataclass
class url_details:
    def __init__(self, url):
       #Importing and creating the object of Url Substrings
       self.url_substrings = URLSubStrings(url)  
       #Assigning the URL from URL substring Constructor to the current class 
       self.url = self.url_substrings.url        
       #Getting the URL domain from the URL SubStrings class
       self.url_domain = self.url_substrings.url_domain()     
       self.url_path_file = self.url_substrings.url_path_file()
       self.url_parameters = self.url_substrings.url_parameters()
       self.url_directory = self.url_substrings.url_directory()
       #To avoid Path/File and Directory are same.
       if self.url_path_file == self.url_directory:
           self.url_path_file = None
           
    #Creating 5 different methods to claculate the length for different parts of URL
    def url_length(self):
        length_url = len(self.url)
        return length_url
    
    def domain_length(self):
        domain_length = len(self.url_domain)
        return domain_length
    
    def directory_length(self):
        directory_length = len(self.url_directory)
        return directory_length
    
    def file_path_length(self):
        if self.url_path_file is None:
            self.url_path_file = ""
        file_length = len(self.url_path_file)
        return file_length
    
    def params_length(self):
        params_length = len(self.url_parameters)
        return params_length
        
    def qty_tld_url(self):
        try:
            tld = self.url_domain.split('.')[-1]
            return len(tld)
        except Exception as e:
            raise CustomException(e, sys)
        
    def qty_params(self):
        try:
            parsed_url = urlparse(self.url)
            query_params = parse_qs(parsed_url.query)
            return sum(len(values) for values in query_params.values())
        except Exception as e:
            raise CustomException(e, sys)
        
    def qty_vowels_domain(self):
        try:
            # Defining Vowels
            vowels = ["a", "e", "i", "o", "u"]
            #initialize the sign count
            vowels_counts = 0
            # Split Domain in words
            words = self.url_domain.split()
            
            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in vowels:
                        vowels_counts += 1
                        
            # Return the the dictionary of sign counts
            return vowels_counts  
            
        except Exception as e:
            raise CustomException(e, sys)
            
    def tld_present_params(self):
        try:
            # Assgining the mentioned TLD int the Domain
            tld = "." + self.url_domain.split(".")[-1]
            # Checking if Parameter has TLD in it
            if tld in self.url_parameters:
                return 1
            else:
                return 0
        except Exception as e:
            raise CustomException(e, sys)
                        

    def count_signs_in_url(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]
            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            # Split the URL into words
            words = self.url.split()
            
            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1
             
            return sign_counts
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_domain(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            
            words = self.url_domain

            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1
            return sign_counts
            logging.info("Counted the number of signs in URL Domain")
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_directory(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}

            # Iterate over each character in the URL directory
            for char in self.url_directory:
                # If the character is a sign, increment its count
                if char in signs:
                    sign_counts[char] += 1

            return sign_counts

        except Exception as e:
            raise CustomException(e, sys)

        
    def count_signs_in_url_path_file(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            
            # If URL directory is None, return the empty sign counts
            if self.url_path_file is None:
                return sign_counts
            else:
                words = self.url_path_file

                # Iterate over each word
                for word in words:
                    # Iterate over each character in the word
                    for char in word:
                        # If the character is a sign, increment its count
                        if char in signs:
                            sign_counts[char] += 1   
                            
                    # Return the sign counts
                return sign_counts
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_parameters(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            
            words = self.url_parameters

            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1
            
                # Return the sign counts
                return sign_counts  

            # Return the sign counts
            return sign_counts  
            logging.info("Counted the number of signs in URL Parameters")
            
        except Exception as e:
            raise CustomException(e, sys)




if __name__ == "__main__":
    url1 = "https://twitter.com/home"
    url = url_details(url1)
    print(url.count_signs_in_url_parameters())
    print(url.count_signs_in_url_path_file())
    print(url.count_signs_in_url_directory())
    print(url.count_signs_in_url_domain())
    print(url.count_signs_in_url())
    print("url_substrings_length", url.url_length(), "domain_length", url.domain_length(),
                "directory_length", url.directory_length(), "file legth", url.file_path_length(), 
                        "params_legth", url.params_length())
    print("qty_tld_url", url.qty_tld_url())
    print(url.qty_vowels_domain())
    print("tld_present_params", url.tld_present_params())
    print("qty_params", url.qty_params())