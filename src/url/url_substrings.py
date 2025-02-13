from urllib.parse import parse_qs, urlparse


class URLSubStrings:
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)

    def url_scheme(self):
        return self.parsed_url.scheme

    def url_domain(self):
        return self.parsed_url.netloc

    def url_path_file(self):
        return self.parsed_url.path.split("/")[-1]

    def url_directory(self):
        return self.parsed_url.path.split("/")[1]

    def url_parameters(self):
        query = self.parsed_url.query
        return query


if __name__ == "__main__":
    # Example usage:
    url = "www.twitter.com/home"
    details = URLSubStrings(url)
    print("Scheme:", details.url_scheme())
    print("Domian:", details.url_domain())
    print("Path/File:", details.url_path_file())
    print("Directory:", details.url_directory())
    print("Parameters:", details.url_parameters())
    print(details.url_scheme() + "://" + details.url_domain())
