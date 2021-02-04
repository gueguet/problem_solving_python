# https://www.codewars.com/kata/5fee4559135609002c1a1841/train/python

import re
global long_url

def url_shortener(long_url):
  long_url = long_url
  pattern = r"(www.)(.+)(\.)"
  re_match = re.search(pattern, long_url)
  short_url = "short.ly/" + re_match.group(2)
  return short_url


def url_redirector(short_url):
  print(short_url)
  return long_url


if __name__ == "__main__":
  url_shortener("https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e")