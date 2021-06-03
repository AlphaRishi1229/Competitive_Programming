import hashlib

class Codec:

    def __init__(self) -> None:
        """Init for codec."""
        self.url_mapper = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded_url = "http://tinyurl.com/" + hashlib.sha256(longUrl.encode("UTF-8")).hexdigest()[:7]
        self.url_mapper[encoded_url] = longUrl
        return encoded_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_mapper[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))