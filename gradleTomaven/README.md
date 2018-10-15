# Usage:
Maven's file structure of local dependencies is different from gradle. For gradle, the jar and pom are in files named by hash values.
This script help to transform the local dependencies structure of gradle to maven.
# Command:
First of all, download the script
```shell
git clone https://github.com/9plus/scripts.git [fielname]
```
Then put this script in USER_HOME/.gradle/cache/modules-2/files-2.1/, and
```shell
python tramsform.py
```
The result is in ./out.
