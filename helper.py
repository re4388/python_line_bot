import requests, re
from bs4 import BeautifulSoup
from jenkinsapi import api as API
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build
from pprint import pprint







def _get_server_instance():
    jenkins_url = 'http://10.0.4.52:3080/'
    server = Jenkins(jenkins_url, username='gitadmin', password='muengit')
    return server

def get_build_info(last_number=0):
    server = _get_server_instance()
    job = server.get_job('build')
    last_one_build = job.__dict__['_data']['builds'][last_number]
    url = last_one_build['url']
    number = last_one_build['number']
    obj = Build(url, number, job)
    para = obj.get_params()
    print(para)
    repo_name = para['REPO_NAME']
    pjt_name = para['PROJECT_NAME']
    status = obj.get_status()
    timestamp = obj.get_timestamp().strftime("%Y-%m-%d %H:%M:%S")
    return (timestamp, repo_name, pjt_name, number, status)



def get_build_result_from_jenkins():
    text = ""
    text += str(get_build_info(last_number=0))
    text += '\n'
    text += str(get_build_info(last_number=1))
    text += '\n'
    text += str(get_build_info(last_number=2))
    text += '\n'
    text += str(get_build_info(last_number=3))
    text += '\n'
    text += str(get_build_info(last_number=4))
    return text



def apple_news():
    target_url = 'https://tw.appledaily.com/new/realtime'
    print('Start parsing appleNews....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('.rtddt a'), 0):
        if index == 5:
            return content
        link = data['href']
        content += '{}\n\n'.format(link)
    return content






def apple_news():
    target_url = 'https://tw.appledaily.com/new/realtime'
    print('Start parsing appleNews....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('.rtddt a'), 0):
        if index == 5:
            return content
        link = data['href']
        content += '{}\n\n'.format(link)
    return content


def eyny_movie():
    target_url = 'http://www.eyny.com/forum-205-1.html'
    print('Start parsing eynyMovie....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for titleURL in soup.select('.bm_c tbody .xst'):
        if pattern_mega(titleURL.text):
            title = titleURL.text
            if '11379780-1-3' in titleURL['href']:
                continue
            link = 'http://www.eyny.com/' + titleURL['href']
            data = '{}\n{}\n\n'.format(title, link)
            content += data
    return content




def pattern_mega(text):
    patterns = [
        'mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ',
        'ｍｅ', 'ｍｕ', 'ｍｅｇａ', 'GD', 'MG', 'google',
    ]
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True

