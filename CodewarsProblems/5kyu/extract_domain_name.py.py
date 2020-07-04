# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python


import re 
import unittest




def domain_name(url):

    if (url[0] == "h"):
        if ("-" in url):
            pattern = "https?://(www\.)?((?:\w+-)+\w+)(\.\w+)"
            result = re.match(pattern, url)
            return result.group(2)

        pattern = "https?://(www\.)?(\w+)(\.\w+)"
        result = re.match(pattern, url)
        return result.group(2)

    if (url[0] == "w"):

        if ("-" in url):
            pattern = "https?://(www\.)?((?:\w+-)+\w+)(\.\w+)"
            result = re.match(pattern, url)
            return result.group(2)

        else:
            pattern = "(www\.)(\w+)(\.\w+)"
            result = re.match(pattern, url)
            return result.group(2)

    else:
        pattern = "(\w+)(\.\w+)"
        result = re.match(pattern, url)
        return result.group(1)


# test 


class Test(unittest.TestCase):

    def test_domain_name(self):

        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(domain_name("https://hyphen-site.org"), "hyphen-site")


if __name__ == "__main__":
    unittest.main()



# my version is not very clean... I'm not a regex master at all

# short version 
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


# detail version
def domain_name(url):
    from re import findall, VERBOSE

    try:
        url = findall("""\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing
                        
                        (?: www.)?    # matches www. or nothing
                        
                        ([- a-z]+)    # matches a sequence of letters and dashes
                        
                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]

    except:
        return "Invalid URL."
