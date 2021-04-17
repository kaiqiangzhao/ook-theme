#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import locale

# 基本信息
AUTHOR = 'XXX'
SITENAME = 'XXX'
SITEURL = ''  # 无需填写
MYEMAIL = 'XXX'

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
    ('github', 'XXX'),
    ('email', '#mail'),
    ('zhihu', 'XXX'),
)

DEFAULT_PAGINATION = 8

# 文章所在路径
PATH = 'content'

# 主题
THEME = 'theme/ookcafe'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
USER_LOGO_URL = "https://avatars.githubusercontent.com/u/38523576?v=4"

# 生成的静态文件路径
OUTPUT_PATH = "output"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None