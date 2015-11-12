from distutils.core import setup
setup(
  name = 'djangorestversioning',
  packages = ['djangorestversioning'],
  version = '0.2.2',
  license='MIT',
  description = 'A lightweight mixin to allow routing Django Rest Framework endpoints to different classes depending on version.',
  author = 'Craig Tweedy',
  author_email = 'ahoy@craigtweedy.co.uk',
  url = 'https://github.com/craigtweedy/django-rest-versioning',
  download_url = 'https://github.com/craigtweedy/django-rest-versioning/tarball/0.2.2',
  keywords = ['django', 'django-rest-framework', 'version', 'versioning', 'api'],
  classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
