# Usage:
Maven的本地依赖仓的文件结构与Gradle的本地依赖仓结构相似，让Gradle直接识别本地的maven仓的包可以使用这个脚本
# Steps:
首先在build.gradle文件里添加如下代码
```
buildscript{
  repositories{
    mavenLocal()
  }
  dependencies{
  }
}
```
然后下载脚本
```shell
git clone https://github.com/9plus/scripts.git [fielname]
```
将脚本文件放在USER_HOME/.gradle/caches/modules-2/files-2.1/下
```shell
python tramsform.py
```
结果在out目录中
