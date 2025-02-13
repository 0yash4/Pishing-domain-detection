from dataclasses import dataclass

import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.url.url_credentials import url_credentials
from src.url.url_details import url_details


@dataclass
class classes_initailization:
    def __init__(self, url):
        # Initializing All the imported classes
        self.url_credentials = url_credentials(url)
        self.url_details = url_details(url)
        

class CustomDataURL:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_url: int = self.classes_initailization.url_details.count_signs_in_url()["."]
        self.qty_hyphen_url: int = self.classes_initailization.url_details.count_signs_in_url()["-"]
        self.qty_underline_url: int = self.classes_initailization.url_details.count_signs_in_url()["_"]
        self.qty_slash_url: int = self.classes_initailization.url_details.count_signs_in_url()["/"]
        self.qty_questionmark_url: int = self.classes_initailization.url_details.count_signs_in_url()["?"]
        self.qty_equal_url: int = self.classes_initailization.url_details.count_signs_in_url()["="]
        self.qty_at_url: int = self.classes_initailization.url_details.count_signs_in_url()["@"]
        self.qty_and_url: int = self.classes_initailization.url_details.count_signs_in_url()["&"]
        self.qty_exclamation_url: int = self.classes_initailization.url_details.count_signs_in_url()["!"]
        self.qty_space_url: int = self.classes_initailization.url_details.count_signs_in_url()[" "]
        self.qty_tilde_url: int = self.classes_initailization.url_details.count_signs_in_url()["∼"]
        self.qty_comma_url: int = self.classes_initailization.url_details.count_signs_in_url()[","]
        self.qty_plus_url: int = self.classes_initailization.url_details.count_signs_in_url()["+"]
        self.qty_asterisk_url: int = self.classes_initailization.url_details.count_signs_in_url()["*"]
        self.qty_hashtag_url: int = self.classes_initailization.url_details.count_signs_in_url()["#"]
        self.qty_dollar_url: int = self.classes_initailization.url_details.count_signs_in_url()["$"]
        self.qty_percent_url: int = self.classes_initailization.url_details.count_signs_in_url()["%"]
        self.qty_tld_url: int = self.classes_initailization.url_details.qty_tld_url()
        self.length_url: int = self.classes_initailization.url_details.url_length()
        
    def df_url(self):
        data = {
            'qty_dot_url': [self.qty_dot_url],
            'qty_hyphen_url': [self.qty_hyphen_url],
            'qty_underline_url': [self.qty_underline_url],
            'qty_slash_url': [self.qty_slash_url],
            'qty_questionmark_url': [self.qty_questionmark_url],
            'qty_equal_url': [self.qty_equal_url],
            'qty_at_url': [self.qty_at_url],
            'qty_and_url': [self.qty_and_url],
            'qty_exclamation_url': [self.qty_exclamation_url],
            'qty_space_url': [self.qty_space_url],
            'qty_tilde_url': [self.qty_tilde_url],
            'qty_comma_url': [self.qty_comma_url],
            'qty_plus_url': [self.qty_plus_url],
            'qty_asterisk_url': [self.qty_asterisk_url],
            'qty_hashtag_url': [self.qty_hashtag_url],
            'qty_dollar_url': [self.qty_dollar_url],
            'qty_percent_url': [self.qty_percent_url],
            'qty_tld_url': [self.qty_tld_url],
            'length_url': [self.length_url]
        }
        df_url = pd.DataFrame(data)
        return df_url

class CustomDataDomain:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["."]
        self.qty_hyphen_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["-"]
        self.qty_underline_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["_"]
        self.qty_slash_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["/"]
        self.qty_questionmark_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["?"]
        self.qty_equal_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["="]
        self.qty_at_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["@"]
        self.qty_and_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["&"]
        self.qty_exclamation_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["!"]
        self.qty_space_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()[" "]
        self.qty_tilde_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["∼"]
        self.qty_comma_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()[","]
        self.qty_plus_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["+"]
        self.qty_asterisk_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["*"]
        self.qty_hashtag_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["#"]
        self.qty_dollar_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["$"]
        self.qty_percent_domain: int = self.classes_initailization.url_details.count_signs_in_url_domain()["%"]
        self.qty_vowels_domain: int = self.classes_initailization.url_details.qty_vowels_domain()
        self.domain_length: int = self.classes_initailization.url_details.domain_length()
        self.domain_in_ip: bool = self.classes_initailization.url_credentials.domain_in_ip()
        self.server_client_domain: bool = self.classes_initailization.url_credentials.server_client_domain()      
        
    def df_domain(self):
        data = {
            'qty_dot_domain': [self.qty_dot_domain],
            'qty_hyphen_domain': [self.qty_hyphen_domain],
            'qty_underline_domain': [self.qty_underline_domain],
            'qty_slash_domain': [self.qty_slash_domain],
            'qty_questionmark_domain': [self.qty_questionmark_domain],
            'qty_equal_domain': [self.qty_equal_domain],
            'qty_at_domain': [self.qty_at_domain],
            'qty_and_domain': [self.qty_and_domain],
            'qty_exclamation_domain': [self.qty_exclamation_domain],
            'qty_space_domain': [self.qty_space_domain],
            'qty_tilde_domain': [self.qty_tilde_domain],
            'qty_comma_domain': [self.qty_comma_domain],
            'qty_plus_domain': [self.qty_plus_domain],
            'qty_asterisk_domain': [self.qty_asterisk_domain],
            'qty_hashtag_domain': [self.qty_hashtag_domain],
            'qty_dollar_domain': [self.qty_dollar_domain],
            'qty_percent_domain': [self.qty_percent_domain],
            'qty_vowels_domain': [self.qty_vowels_domain],
            'domain_length': [self.domain_length],
            'domain_in_ip': [self.domain_in_ip],
            'server_client_domain': [self.server_client_domain]
        }
        df_domain = pd.DataFrame(data)
        return df_domain

class CustomDataDirectory:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["."]
        self.qty_hyphen_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["-"]
        self.qty_underline_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["_"]
        self.qty_slash_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["/"]
        self.qty_questionmark_directory: int= self.classes_initailization.url_details.count_signs_in_url_directory()["?"]
        self.qty_equal_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["="]
        self.qty_at_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["@"]
        self.qty_and_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["&"]
        self.qty_exclamation_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["!"]
        self.qty_space_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()[" "]
        self.qty_tilde_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["∼"]
        self.qty_comma_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()[","]
        self.qty_plus_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["+"]
        self.qty_asterisk_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["*"]
        self.qty_hashtag_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["#"]
        self.qty_dollar_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["$"]
        self.qty_percent_directory: int = self.classes_initailization.url_details.count_signs_in_url_directory()["%"]
        self.directory_length: int = self.classes_initailization.url_details.directory_length()
        
    def df_directory(self):
        data = {
            'qty_dot_directory': [self.qty_dot_directory],
            'qty_hyphen_directory': [self.qty_hyphen_directory],
            'qty_underline_directory': [self.qty_underline_directory],
            'qty_slash_directory': [self.qty_slash_directory],
            'qty_questionmark_directory': [self.qty_questionmark_directory],
            'qty_equal_directory': [self.qty_equal_directory],
            'qty_at_directory': [self.qty_at_directory],
            'qty_and_directory': [self.qty_and_directory],
            'qty_exclamation_directory': [self.qty_exclamation_directory],
            'qty_space_directory': [self.qty_space_directory],
            'qty_tilde_directory': [self.qty_tilde_directory],
            'qty_comma_directory': [self.qty_comma_directory],
            'qty_plus_directory': [self.qty_plus_directory],
            'qty_asterisk_directory': [self.qty_asterisk_directory],
            'qty_hashtag_directory': [self.qty_hashtag_directory],
            'qty_dollar_directory': [self.qty_dollar_directory],
            'qty_percent_directory': [self.qty_percent_directory],
            'directory_length': [self.directory_length]
        }
        df_directory = pd.DataFrame(data)
        return df_directory

class CustomDataFile:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["."]
        self.qty_hyphen_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["-"]
        self.qty_underline_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["_"]
        self.qty_slash_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["/"]
        self.qty_questionmark_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["?"]
        self.qty_equal_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["="]
        self.qty_at_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["@"]
        self.qty_and_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["&"]
        self.qty_exclamation_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["!"]
        self.qty_space_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()[" "]
        self.qty_tilde_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["∼"]
        self.qty_comma_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()[","]
        self.qty_plus_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["+"]
        self.qty_asterisk_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["*"]
        self.qty_hashtag_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["#"]
        self.qty_dollar_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["$"]
        self.qty_percent_file: int = self.classes_initailization.url_details.count_signs_in_url_path_file()["%"]
        self.file_length: int = self.classes_initailization.url_details.file_path_length()        
        
    def df_file(self):
        data = {
            'qty_dot_file': [self.qty_dot_file],
            'qty_hyphen_file': [self.qty_hyphen_file],
            'qty_underline_file': [self.qty_underline_file],
            'qty_slash_file': [self.qty_slash_file],
            'qty_questionmark_file': [self.qty_questionmark_file],
            'qty_equal_file': [self.qty_equal_file],
            'qty_at_file': [self.qty_at_file],
            'qty_and_file': [self.qty_and_file],
            'qty_exclamation_file': [self.qty_exclamation_file],
            'qty_space_file': [self.qty_space_file],
            'qty_tilde_file': [self.qty_tilde_file],
            'qty_comma_file': [self.qty_comma_file],
            'qty_plus_file': [self.qty_plus_file],
            'qty_asterisk_file': [self.qty_asterisk_file],
            'qty_hashtag_file': [self.qty_hashtag_file],
            'qty_dollar_file': [self.qty_dollar_file],
            'qty_percent_file': [self.qty_percent_file],
            'file_length': [self.file_length]
        }
        df_file = pd.DataFrame(data)
        return df_file

class CustomDataParams:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["."]
        self.qty_hyphen_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["-"]
        self.qty_underline_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["_"]
        self.qty_slash_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["/"]
        self.qty_questionmark_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["?"]
        self.qty_equal_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["="]
        self.qty_at_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["@"]
        self.qty_and_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["&"]
        self.qty_exclamation_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["!"]
        self.qty_space_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()[" "]
        self.qty_tilde_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["∼"]
        self.qty_comma_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()[","]
        self.qty_plus_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["+"]
        self.qty_asterisk_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["*"]
        self.qty_hashtag_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["#"]
        self.qty_dollar_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["$"]
        self.qty_percent_params: int = self.classes_initailization.url_details.count_signs_in_url_parameters()["%"]
        self.params_length: int = self.classes_initailization.url_details.params_length()
        self.tld_present_params: bool = self.classes_initailization.url_details.tld_present_params()
        self.qty_params: int = self.classes_initailization.url_details.qty_params()

    def df_params(self):
        data = {
            'qty_dot_params': [self.qty_dot_params],
            'qty_hyphen_params': [self.qty_hyphen_params],
            'qty_underline_params': [self.qty_underline_params],
            'qty_slash_params': [self.qty_slash_params],
            'qty_questionmark_params': [self.qty_questionmark_params],
            'qty_equal_params': [self.qty_equal_params],
            'qty_at_params': [self.qty_at_params],
            'qty_and_params': [self.qty_and_params],
            'qty_exclamation_params': [self.qty_exclamation_params],
            'qty_space_params': [self.qty_space_params],
            'qty_tilde_params': [self.qty_tilde_params],
            'qty_comma_params': [self.qty_comma_params],
            'qty_plus_params': [self.qty_plus_params],
            'qty_asterisk_params': [self.qty_asterisk_params],
            'qty_hashtag_params': [self.qty_hashtag_params],
            'qty_dollar_params': [self.qty_dollar_params],
            'qty_percent_params': [self.qty_percent_params],
            'params_length': [self.params_length],
            'tld_present_params': [self.tld_present_params],
            'qty_params': [self.qty_params]
        }
        df_params = pd.DataFrame(data)
        return df_params
    
class CustomDataCredentials:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.email_in_url: bool = self.classes_initailization.url_credentials.email_in_url()
        self.time_response: int = self.classes_initailization.url_credentials.time_response()
        self.domain_spf: bool = self.classes_initailization.url_credentials.domain_spf()
        self.asn_ip: int = self.classes_initailization.url_credentials.asn_ip()
        self.time_domain_activation, self.time_domain_expiration = self.classes_initailization.url_credentials.time_domain_activation_expiration()
        self.qty_ip_resolved: int = self.classes_initailization.url_credentials.qty_ip_resolved()
        self.qty_nameservers: int = self.classes_initailization.url_credentials.qty_nameservers()
        self.qty_mx_servers: int = self.classes_initailization.url_credentials.qty_mx_servers()
        self.ttl_hostname: int = self.classes_initailization.url_credentials.ttl_hostname()
        self.tls_ssl_certificate: bool = self.classes_initailization.url_credentials.tls_ssl_certificate()
        self.qty_redirects: int = self.classes_initailization.url_credentials.qty_redirects()
        self.url_google_index: bool = self.classes_initailization.url_credentials.url_google_index()
        self.domain_google_index: bool = self.classes_initailization.url_credentials.domain_google_index()
        self.url_shortened: bool = self.classes_initailization.url_credentials.url_shortened()
        
    def df_credentials(self):
        data = {
            'email_in_url': [self.email_in_url],
            'time_response': [self.time_response],
            'domain_spf': [self.domain_spf],
            'asn_ip': [self.asn_ip],
            'time_domain_activation': [self.time_domain_activation],
            'time_domain_expiration': [self.time_domain_expiration],
            'qty_ip_resolved': [self.qty_ip_resolved],
            'qty_nameservers': [self.qty_nameservers],
            'qty_mx_servers': [self.qty_mx_servers],
            'ttl_hostname': [self.ttl_hostname],
            'tls_ssl_certificate': [self.tls_ssl_certificate],
            'qty_redirects': [self.qty_redirects],
            'url_google_index': [self.url_google_index],
            'domain_google_index': [self.domain_google_index],
            'url_shortened': [self.url_shortened]
        }
        df_credentials = pd.DataFrame(data)
        return df_credentials

class custom_final_df:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.custom_data_url = CustomDataURL(url)
        self.custom_data_domain = CustomDataDomain(url)
        self.custom_data_directory = CustomDataDirectory(url)
        self.custom_data_file = CustomDataFile(url)
        self.custom_data_params = CustomDataParams(url)
        self.custom_data_credentials = CustomDataCredentials(url)
        self.length_url = self.classes_initailization.url_details.url_length()
        
    def final_df(self):
        df_url = self.custom_data_url.df_url()
        df_domain = self.custom_data_domain.df_domain()
        df_directory = self.custom_data_directory.df_directory()
        df_file = self.custom_data_file.df_file()
        df_params = self.custom_data_params.df_params()
        df_credentials = self.custom_data_credentials.df_credentials()
        
        final_df = pd.concat([df_url, df_domain, df_directory, df_file, df_params, df_credentials], axis=1)
        #final_df["url_shortened"] = 0
        #df = final_df.drop(columns="email_in_url", axis=1)
        return final_df


if __name__ == "__main__":
    url1 = input("Url: ")
    init = custom_final_df(url1)
    print(init.final_df())