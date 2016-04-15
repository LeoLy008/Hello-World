# Tushare
2016-01-30
[python金融包](http://tushare.org/index.html)

**装后感: 开源对 window 无爱**

## 安装
1. python
2. pandas
3. lxml

提示可以安装 Anaconda 免去独立安装 pandas 及 lxml，但看了 Anaconda 后觉得没必要安装这玩意(^o^)<br>

### 安装python3.5.1
直接下载安装x64的
安装完成后 pip 提示有新版本，乖乖升级下
如下:
```cmd
F:\study\log>pip --version
pip 7.1.2 from f:\python35\lib\site-packages (python 3.5)

F:\study\log>where pip
F:\Python35\Scripts\pip.exe

F:\study\log>pip install
You must give at least one requirement to install (see "pip help install")
You are using pip version 7.1.2, however version 8.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

F:\study\log>python -m pip install --upgrade pip
Collecting pip
  Downloading pip-8.0.2-py2.py3-none-any.whl (1.2MB)
  ...
    Installing collected packages: pip
      Found existing installation: pip 7.1.2
        Uninstalling pip-7.1.2:
          Successfully uninstalled pip-7.1.2
    Successfully installed pip-8.0.2

F:\study\log>pip --version
pip 8.0.2 from f:\python35\lib\site-packages (python 3.5)
```

### 安装lxml
lxml 是python to libxml2 libxlst 的接口，在windows上需要提供对应的binary 版本的，否则无法使用。所以我们用 pypi 安装
```
F:\study\log>pip install lxml==3.5.1
Collecting lxml==3.5.1
  Could not find a version that satisfies the requirement lxml==3.5.1 (from versions: 0.9, 0.
9.1, 0.9.2, 1.0b0, 1.0, 1.0.1, 1.0.2, 1.0.3, 1.0.4, 1.1a0, 1.1b0, 1.1, 1.1.1, 1.1.2, 1.2, 1.2
.1, 1.3b0, 1.3, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 2.0a1, 2.0a2, 2.0a3, 2.0a4, 2.0a5, 2.0a6,
2.0b1, 2.0b2, 2.0, 2.0.1, 2.0.2, 2.0.3, 2.0.4, 2.0.5, 2.0.6, 2.0.7, 2.0.8, 2.0.9, 2.0.10, 2.0
.11, 2.1a1, 2.1b1, 2.1b2, 2.1b3, 2.1, 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.2a1, 2.2b1, 2.2b2,
 2.2b3, 2.2b4, 2.2, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 2.2.7, 2.2.8, 2.3b1, 2.3, 2.3.1
, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6, 3.0, 3.0.1, 3.0.2, 3.1b1, 3.1.0, 3.1.1, 3.1.2, 3.2.0, 3.
2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5, 3.3.0b1, 3.3.0b2, 3.3.0b3, 3.3.0b4, 3.3.0b5, 3.3.0, 3.3.1, 3
.3.2, 3.3.3, 3.3.4, 3.3.5, 3.3.6, 3.4.0, 3.4.1, 3.4.2, 3.4.3, 3.4.4, 3.5.0b1, 3.5.0)
No matching distribution found for lxml==3.5.1
```
试图安装 for python 3.5.1, 没有 那就3.5.0吧

```cmd
F:\study\log>pip install lxml==3.5.0
Collecting lxml==3.5.0
  Downloading lxml-3.5.0.tar.gz (3.8MB)
  ...
  Installing collected packages: lxml
    Running setup.py install for lxml ... error
      Complete output from command f:\python35\python.exe -u -c "import setuptools, tokenize;__
  file__='C:\\Users\\XYuser\\AppData\\Local\\Temp\\pip-build-qfmnkcci\\lxml\\setup.py';exec(com
  pile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'
  ))" install --record C:\Users\XYuser\AppData\Local\Temp\pip-xvnvlnpg-record\install-record.tx
  t --single-version-externally-managed --compile:
      Building lxml version 3.5.0.
      Building without Cython.
      ERROR: b"'xslt-config' \xb2\xbb\xca\xc7\xc4\xda\xb2\xbf\xbb\xf2\xcd\xe2\xb2\xbf\xc3\xfc\x
  c1\xee\xa3\xac\xd2\xb2\xb2\xbb\xca\xc7\xbf\xc9\xd4\xcb\xd0\xd0\xb5\xc4\xb3\xcc\xd0\xf2\r\n\xb
  b\xf2\xc5\xfa\xb4\xa6\xc0\xed\xce\xc4\xbc\xfe\xa1\xa3\r\n"
      ** make sure the development packages of libxml2 and libxslt are installed **


      Using build configuration of libxslt
      running install
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-3.5
      creating build\lib.win-amd64-3.5\lxml
      copying src\lxml\builder.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\cssselect.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\doctestcompare.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\ElementInclude.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\pyclasslookup.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\sax.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\usedoctest.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\_elementpath.py -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\__init__.py -> build\lib.win-amd64-3.5\lxml
      creating build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\__init__.py -> build\lib.win-amd64-3.5\lxml\includes
      creating build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\builder.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\clean.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\defs.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\diff.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\ElementSoup.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\formfill.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\html5parser.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\soupparser.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\usedoctest.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\_diffcommand.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\_html5builder.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\_setmixin.py -> build\lib.win-amd64-3.5\lxml\html
      copying src\lxml\html\__init__.py -> build\lib.win-amd64-3.5\lxml\html
      creating build\lib.win-amd64-3.5\lxml\isoschematron

      copying src\lxml\isoschematron\__init__.py -> build\lib.win-amd64-3.5\lxml\isoschematron
      copying src\lxml\lxml.etree.h -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\lxml.etree_api.h -> build\lib.win-amd64-3.5\lxml
      copying src\lxml\includes\c14n.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\config.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\dtdvalid.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\etreepublic.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\htmlparser.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\relaxng.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\schematron.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\tree.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\uri.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\xinclude.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\xmlerror.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\xmlparser.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\xmlschema.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\xpath.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\xslt.pxd -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\etree_defs.h -> build\lib.win-amd64-3.5\lxml\includes
      copying src\lxml\includes\lxml-version.h -> build\lib.win-amd64-3.5\lxml\includes
      creating build\lib.win-amd64-3.5\lxml\isoschematron\resources
      creating build\lib.win-amd64-3.5\lxml\isoschematron\resources\rng
      copying src\lxml\isoschematron\resources\rng\iso-schematron.rng -> build\lib.win-amd64-3.
  5\lxml\isoschematron\resources\rng
      creating build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl
      copying src\lxml\isoschematron\resources\xsl\RNG2Schtrn.xsl -> build\lib.win-amd64-3.5\lx
  ml\isoschematron\resources\xsl
      copying src\lxml\isoschematron\resources\xsl\XSD2Schtrn.xsl -> build\lib.win-amd64-3.5\lx
  ml\isoschematron\resources\xsl
  copying src\lxml\isoschematron\resources\xsl\RNG2Schtrn.xsl -> build\lib.win-amd64-3.5\lx

ml\isoschematron\resources\xsl
  copying src\lxml\isoschematron\resources\xsl\XSD2Schtrn.xsl -> build\lib.win-amd64-3.5\lx
ml\isoschematron\resources\xsl
  creating build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
  copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_abstract_expand.xsl
-> build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
  copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_dsdl_include.xsl ->
build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
  copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_message.
xsl -> build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
  copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_skeleton
_for_xslt1.xsl -> build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xsl
t1
  copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_svrl_for_xslt1.xsl
-> build\lib.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
  copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\readme.txt -> build\lib
.win-amd64-3.5\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
  running build_ext
  building 'lxml.etree' extension
  error: Unable to find vcvarsall.bat

  ----------------------------------------
Command "f:\python35\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\XYuse
r\\AppData\\Local\\Temp\\pip-build-qfmnkcci\\lxml\\setup.py';exec(compile(getattr(tokenize, '
open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record C:\
Users\XYuser\AppData\Local\Temp\pip-xvnvlnpg-record\install-record.txt --single-version-exter
nally-managed --compile" failed with error code 1 in C:\Users\XYuser\AppData\Local\Temp\pip-b
uild-qfmnkcci\lxml

```
报错了, 试图编译生成二进制包，但是没有 vcvarsall.bat (vs环境无)失败
下载了个 lxml-3.5.0-cp35-none-win_amd64.whl 安装 (Wheels python包)
[lxml Wheels](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml)
```cmd
F:\tools>pip install lxml-3.5.0-cp35-none-win_amd64.whl
Processing f:\tools\lxml-3.5.0-cp35-none-win_amd64.whl
Installing collected packages: lxml
Successfully installed lxml-3.5.0
```

OK，试试
```cmd
F:\tools>python
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win3
2
Type "help", "copyright", "credits" or "license" for more information.
>>> import lxml
>>> help(lxml)
Help on package lxml:

NAME
    lxml - # this is a package
    ...
```

### 安装 pandas
要安装 pandas 需要先安装 [NumPy](http://pandas.pydata.org/)<br>
[NumPy下载地址](http://www.scipy.org/scipylib/download.html)
看了看文档，貌似没有 windows binary 提供。去之前的 whl 站点找找
Lucky, [NumPy + MKL](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy), 122MB, 下来试试

#### 安装 NumPy
```cmd
F:\tools>pip install "numpy-1.11.0b2+mkl-cp35-none-win_amd64.whl"
Processing f:\tools\numpy-1.11.0b2+mkl-cp35-none-win_amd64.whl
Installing collected packages: numpy
Successfully installed numpy-1.11.0b2
```

#### 安装 Pandas
```cmd
F:\tools>pip install pandas==0.17.1
Collecting pandas==0.17.1
  Using cached pandas-0.17.1-cp35-none-win_amd64.whl
Requirement already satisfied (use --upgrade to upgrade): numpy>=1.7.0 in f:\python35\lib\sit
e-packages (from pandas==0.17.1)
Collecting pytz>=2011k (from pandas==0.17.1)
  Using cached pytz-2015.7-py2.py3-none-any.whl
Collecting python-dateutil>=2 (from pandas==0.17.1)
  Using cached python_dateutil-2.4.2-py2.py3-none-any.whl
Collecting six>=1.5 (from python-dateutil>=2->pandas==0.17.1)
  Using cached six-1.10.0-py2.py3-none-any.whl
Installing collected packages: pytz, six, python-dateutil, pandas

Successfully installed pandas-0.17.1 python-dateutil-2.4.2 pytz-2015.7 six-1.10.0
```

## 安装 Tushare
```cmd
F:\tools>pip install tushare==0.4.6
Collecting tushare==0.4.6
  Using cached tushare-0.4.6.zip
Installing collected packages: tushare
  Running setup.py install for tushare ... done
Successfully installed tushare-0.4.6
```

测试
```cmd
```

## 安装 sqlalchemy for mysql connection, 2016-03-30
```cmd
F:\study\log>pip install sqlalchemy
Collecting sqlalchemy
  Downloading SQLAlchemy-1.0.12.tar.gz (4.7MB)
    100% |████████████████████████████████| 4.8MB 54kB/s
Installing collected packages: sqlalchemy
  Running setup.py install for sqlalchemy ... done
Successfully installed sqlalchemy-1.0.12
You are using pip version 8.0.2, however version 8.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

## 安装 pymysql
```cmd
F:\study\log>pip install pymysql
Collecting pymysql
  Downloading PyMySQL-0.7.2-py2.py3-none-any.whl (76kB)
    100% |████████████████████████████████| 77kB 954kB/s
Installing collected packages: pymysql
Successfully installed pymysql-0.7.2
You are using pip version 8.0.2, however version 8.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

## 使用 sqlalchemy + pymysql 链接db
``` python
import sqlalchemy as sqlal

engine = sqlal.create_engine('mysql+pymsql://user:password@host/schema?charset=utf8')

```
