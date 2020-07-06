# https://www.codewars.com/kata/58ab2ed1acbab2eacc00010e/train/python

# webpage : https://www.codewars.com/users/jhoffner


from bs4 import BeautifulSoup
import urllib.request
import re
import ssl 
import unittest

ssl._create_default_https_context = ssl._create_unverified_context # ignore certificates ssl 

def get_member_since(username):

    response = urllib.request.urlopen('https://www.codewars.com/users/{}'.format(username))
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    div_to_regex = ""
    stat_divs = soup.findAll("div", {"class": "stat"})
    for div in stat_divs:
        if "Member Since" in str(div):
            div_to_regex = str(div)

    pattern = "(\/b>)(.+?)(?=</div)"

    # res_username = re.match(pattern, username_info).group(2)
    res_date = re.findall(pattern, div_to_regex)[0][1]

    return res_date

    

# test 

class Test(unittest.TestCase):

    def test_member_since(self):

        self.assertEqual(get_member_since('jhoffner'), 'Oct 2012')
        self.assertEqual(get_member_since('ecolban'), 'Mai 2015')




if __name__ == "__main__":
    unittest.main()
    
