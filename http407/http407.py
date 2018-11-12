import re
import os


"""
the mirror I use is
<mirror>
    <id>nexus-aliyun</id>
    <mirrorOf>central</mirrorOf>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/repositories/central</url>
</mirror>
"""


"""
@path: path of temp.txt, to get the url information
@count: for flag
"""
def read_data(path,id,mirrorOf):
    count=0
    regex407 = re.compile('Downloading from {}: (.*)'.format(id))
    while True:
        count+=1
        print('<-----------trun {} ----------->'.format(count))
        print('<-----------trun {} ----------->'.format(count))
        print('<-----------trun {} ----------->'.format(count))
        print('<-----------trun {} ----------->'.format(count))
        print('<-----------trun {} ----------->'.format(count))
        print('<-----------trun {} ----------->'.format(count))
        print('<-----------trun {} ----------->'.format(count))
        os.system('mvn clean install > {}'.format(path))
        with open((os.path.join(path)), 'r') as f:
            data = f.read()
        urls = regex407.findall(data)
        if not urls:
            break
        else:
            for url in urls:
                #traverse every url
                print(url.split('/'))

                #get file path and directory path
                dir_path= url[url.find('{}/'.format(mirrorOf))+8:find_last(url,'/')]
                file_path= url[find_last(url,'/')+1:]

                #cp file to .m2/repository
                os.system('wget {}'.format(url))
                os.system('rm -rf ~/.m2/repository/{}'.format(file_path))
                os.system('cp -rf {} ~/.m2/repository/{}/'.format(file_path, dir_path))
                os.system('mv {} out/'.format(file_path))

                #print the file you need
                print('run command {}...'.format('cp -rf {} ~/.m2/repository/{}/'.format(file_path, dir_path)))


"""
split url
@path: the url of file
@str: the split character
@return: the last position of the str in url 
"""
def find_last(path, str):
    last_position=-1
    while True:
        position= path.find(str,last_position+1)
        if(position==-1):
            return last_position
        last_position=position

if __name__ == '__main__':
    os.system('touch temp.txt & mkdir out')
    id='nexus-aliyun'
    mirrorOf='central'
    read_data('{}/temp.txt'.format(os.getcwd()),id,mirrorOf)
    os.system('rm -rf temp.txt')