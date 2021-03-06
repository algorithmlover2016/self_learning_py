#!/bin/python
#-*-coding:utf-8 -*-
import functools

def paramLimit(func):
    # http://book.pythontips.com/en/latest/args_and_kwargs.html
    def wrapper(*args, **kwargs):
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func(*args, **kwargs)
    return wrapper

def logging(level):
    def wrapper(func):
        # if not write this sentence, this will change the __name__ of
        # the function who call the decorator
        # https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                    level = level, func = func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log("execute")
@logging(level = 'INFO')
def say(something):
    print "say {}!".format(something)

@paramLimit
@logging(level = "DEBUG")
def do(something):
    print "do {}!".format(something)

# https://www.jb51.net/article/134148.htm
class Rectangle(object):
    def __init__(self, width = 100, height = 100):
        # self._width = width
        # self._height = height
        self.width = width
        self.height = height
        print "init call to init width and height"

    #get method
    @property
    def width(self):
        return self._width

    #set method
    @width.setter
    def width(self, input_width):
        self._width = input_width

    @width.deleter
    def width(self):
        del self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, input_height):
        if not isinstance(input_height, int):
            raise ValueError("input parameter must be int")
        if 0 <= input_height <= 1000:
            self._height = input_height;
        else:
            raise ValueError("input parameter is out of range")
        self._height = input_height;

    @height.deleter
    def height(self):
        del self._height

#decorator in class
class loggingcls(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print "[DEBUG]: enter function {func}()".format(
                func = self.func.__name__)
        return self.func(*args, **kwargs)

@loggingcls
def saycls(something):
    print "say {}!".format(something)

# https://www.cnblogs.com/cicaday/p/python-decorator.html
class loggingpara(object):
    def __init__(self, level = "INFO"):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                    level = self.level, func = func.__name__)
            func(*args, **kwargs)
        return wrapper

@loggingpara(level = "INFO")
def saypara(something):
    print "say {}!".format(something)

# descriptor

class classproperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, klass):
        return self.func(klass)

class DBManage(object):

    @classmethod
    def table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def select_all(cls):
        sql = "SELECT * FROM %s""" % cls.table_name()
        return sql


class DBManageProperty(object):

    @classproperty
    def table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def select_all(cls):
        sql = "SELECT * FROM %s""" % cls.table_name
        return sql

class User(DBManage):
    pass

class Post(DBManage):
    pass


if __name__ == "__main__":
    say("hello")
    do("my work")

    print say.__name__

    s = Rectangle()
    print(s.width, s.height)

    s.width = 1024
    s.height = 768
    print(s.width, s.height)

    #  s.height = 176.8
    #  print(s.width, s.height)
    #
    #  s.height = 1768
    #  print(s.width, s.height)

    saycls("something cls")
    saypara("something parameter")

