from urllib.parse import urlparse


def get_domain(url):
    parse_result = urlparse(url)
    print(parse_result.netloc)
    resfile = open('domain.txt', 'a+')
    resfile.write(str(parse_result.netloc)+'\n')
    resfile.close()


file = open('temp.txt', 'r')

for line in file:
    get_domain(line)
