AUTHOR = 'non4to'
SITENAME = 'Felipe Nonato'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'pelican-themes/pelican-blue'

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/felipesobraljr/'),
          ('github', 'https://github.com/non4to'),
          ('bluesky', 'https://bsky.app/profile/non4to.bsky.social'),
          ('mastodon', 'https://sigmoid.social/@djuniou'),
          ('gamepad', 'https://non4to.itch.io/'),
          ('envelope', 'mailto:felipencsj@gmail.com')
          )

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SIDEBAR_DIGEST = 'Phd Student - University of Tsukuba'

AVATAR = 'images/avatar.jpeg'

STATIC_PATHS = ['images']

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 10

INDEX_SAVE_AS = 'blog.html'

ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

MENUITEMS = (
    ('Home', '/'),
    ('Blog', '/blog.html'),
)