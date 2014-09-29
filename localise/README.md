Localise
========

Unlike the other parts of this repo, this isn't a style or theme.  It's a tool for using with existing styles or, really, any CSS file.  It takes the source file, locates all the image files (e.g. background-image lines), downloads the images, base64 encodes them and then rewrites the CSS to use that encoded image instead of the URL.


Requirements
------------

* Python 2.7 (will probably work with 2.6, might work with previous versions).
* The [Requests](http://docs.python-requests.org/en/latest/) module.
* Image URLs must be absolute, not relative (especially since they will usually be remote).
