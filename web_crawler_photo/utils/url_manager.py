

class UrlManager:

    def __init__(self):
        self.new_url = set()
        self.old_url = set()



    def add_new_url(self,url):
        if url is None or len(url) == 0:
            return
        if url in self.new_url or url in self.old_url:
            return
        self.new_url.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return

        for new_url in urls:
            self.new_url.add(new_url)

    def get_url(self):
        if self.has_new_url():
            url = self.new_url.pop()
            self.old_url.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return  len(self.new_url) > 0




