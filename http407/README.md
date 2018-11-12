# Usage
当`maven clean install`编译过程中出现`Server returned HTTP response code: 407 for URL`的错误时，参考以下情况：
* 如果需要的文件可以用`wget`命令下载，可以使用本脚本。
* 如果`wget`无法下载所需文件，尝试不用代理或者检查代理的配置是否正确。</br>

PS:在stackoverflow上找了很久也没有找到好的解决办法，只能采用`wget`命令单独下载，编译的时候可能需要下载很多文件，而一个个用`wget`下载然后移到对应的目录太慢了，因此写了这个脚本

# Steps
在任意目录下克隆本仓，执行
```
git clone https://github.com/9plus/scripts.git
```
把`http407`目录下的脚本拷到`maven`编译的目录下，然后根据你的`maven`的mirror配置，修改本脚本的id和mirrorOf，例如如果是如下的阿里云配置，则不需要修改
```
<mirror>
    <id>nexus-aliyun</id>
    <mirrorOf>central</mirrorOf>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/repositories/central</url>
</mirror>
```
然后执行
```
python http407.py
```
代码写的比较死，逻辑也很简单，有需求的可以自己修改
