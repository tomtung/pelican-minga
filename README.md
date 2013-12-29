# Minga

Minga is a simplistic and responsive theme for [Pelican](https://github.com/getpelican/pelican), based on the [Gumby Framework](http://gumbyframework.com/docs). It is a fork of the [Gum](https://github.com/getpelican/pelican-themes/tree/master/gum) theme by [@uknick](https://github.com/uknick), with quite a lot of tweaks and clean-ups, as well as some new features.

### Configuration

Edit your settings file to include the following if desired (any values left blank won't show up in the theme):

```
GITHUB_URL = ''
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''
DOUBAN_URL = ''
WEIBO_URL = ''
```

This theme uses the latest Google Analytics code, which will be included when the following values are filled out appropriately.

```
GOOGLE_ANALYTICS = 'UA-XXXX-YYYY'
```

You can also enable MathJax support by setting the following variable:
```
ENABLE_MATHJAX = True
```

### Development

Please do not edit `static/css/gumby.css` directly. Instead, edit `sass/_custom.scss` instead, and use [Compass](http://compass-style.org/) to compile:

```
compass compile
```

**MIT Open Source License**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
