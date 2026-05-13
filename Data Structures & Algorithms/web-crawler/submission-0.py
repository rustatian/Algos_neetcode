# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from urllib.parse import urlsplit

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []

        start = [startUrl]
        seen = set()
        orighn = urlsplit(startUrl).hostname

        while start:
            l = len(start)

            for _ in range(l):
                url = start.pop()
                if urlsplit(url).hostname != orighn:
                    continue
                if url in seen:
                    continue
                seen.add(url)
                if url not in res:
                    res.append(url)
                urls = htmlParser.getUrls(url)

                for u in urls:
                    if urlsplit(u).hostname != orighn:
                        continue
                    start.append(u)
        return res