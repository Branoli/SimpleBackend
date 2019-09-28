import re

re_class_name = re.compile(r'([A-Z]*[a-z]*)')


def convert_class_name(name):
    li = re_class_name.findall(name)
    return '_'.join(i.lower() for i in li if i)


class classproperty(object):  # noqa
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)
