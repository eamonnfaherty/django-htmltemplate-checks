__author__ = 'eamonnfaherty'
VERSION = (0, 0, 1)


def get_version(svn=False, limit=3):
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION[:limit]])
  
