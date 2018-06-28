# -*- coding: utf-8 -*-


regularC_text ='''/*[C语言 常用正则表达式]*/
匹配函数
first_match=(line=~/([\w\:]+)\(([^\)]*)\)$/)
([\w\:]+)\(([^\)]*)\)$
([\w\:]+)\(([^\)]*)\)\s*?\{?$
^\s*\w+\s+([\w\:]+)\(([^\)]*)\)$
^\w+\s+([\w\:]+)\(([^\)]*)\)$
^([\w\s]+)([\w\:]+)\(([^\)]*)\)$
^([\w\s\*]+)([\w\:\*]+)\(([^\)]*)\)$
^([\w\*]+( )*?){2,}\(([^!@#$+%^;]+?)\)(?!\s*;)


查找函数整体 
^\s*\w+\s+([\w\:]+)\(([^\)]*)\)$\s*\{([\s\S]+?)\s*^\}\s*$
^\w+\s+([\w\:]+)\(([^\)]*)\)$\s*\{([\s\S]+?)\s*^\}\s*$
^([*\w]+)\s+([\w\:\*]+)\(([^\)]*)\)$\s*\{([\s\S]+?)\s*^\}\s*$
^([*\w]+)\s+([\w\:\*\s]+)\(([^\)]*)\)$\s*\{([\s\S]+?)\s*^\}\s*$

'''

def get_regularC_text():
    return regularC_text