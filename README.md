# ookcafe-blog-theme

基于pelican框架开发的静态博客主题

# pelican

pelican是一个使用Python编写的静态网站生成器。

github：https://github.com/getpelican/pelican

文档：https://docs.getpelican.com/en/latest/

# 使用

```
mkdir projectname
cd projectname
pip install "pelican[markdown]"
pelican-quickstart  #需要回答些问题
mkdir theme
```
将ookcafe-blog-theme里的ookcafe文件夹拷贝到projectname/theme

将ookcafe-blog-theme里的pelicanconf_sample.py文件重命名为pelicanconf.py,并替换projectname里的pelicanconf.py文件

自己补全pelicanconf.py文件, 可先修改其中“XXX”部分

然后执行下面的命令，打开输出的网址就可以看到了
```
pelican --listen
```


# demo

![demo](https://github.com/kaiqiangzhao/ook-theme/blob/master/demo.png)
