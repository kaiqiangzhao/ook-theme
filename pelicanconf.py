#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import locale

# 基本信息
AUTHOR = 'xxx'
SITENAME = 'xxx'
SITEURL = ''
MYEMAIL = 'xxx@gmail.com'

# 基本配置
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = locale.getdefaultlocale()[0]

# 导航栏
LINKS = (
    ('首页', '/index.html'),
    ('关于', '/about-me.html'),
    ('归档', '/archives.html'),
    ('标签', '/tags.html'),
)

# 社交链接
SOCIAL = (
    ('github', 'xxx'),
    ('email', '#mail'),
    ('zhihu', 'xxx'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# 博客文章路径
PATH = 'content'
# 主题
THEME = 'theme/ookcafe'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
USER_LOGO_URL = "/theme/imgs/avatar.png"

# output path
OUTPUT_PATH = "xxx"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
