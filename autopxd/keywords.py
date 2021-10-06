# Cython keywords, obtained from cython/Cython/Parser/Grammar with:
# import string
# lines = open('Grammar').readlines()
# lines = '\n'.join(line for line in lines if not line.strip().startswith('#'))
# names = lines.split('\'')[1::2]
# for name in sorted(set(names)):
#     if all(s in string.ascii_letters for s in name):
#         print("'{}',".format(name))

cython_keywords = [
    "DEF",
    "ELIF",
    "ELSE",
    "False",
    "IF",
    "None",
    "True",
    "and",
    "api",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "by",
    "cdef",
    "char",
    "cimport",
    "class",
    "complex",
    "const",
    "continue",
    "cpdef",
    "cppclass",
    "ctypedef",
    "def",
    "del",
    "double",
    "elif",
    "else",
    "enum",
    "except",
    "exec",
    "extern",
    "finally",
    "for",
    "from",
    "fused",
    "gil",
    "global",
    "if",
    "import",
    "in",
    "int",
    "is",
    "lambda",
    "long",
    "namespace",
    "new",
    "nogil",
    "nonlocal",
    "not",
    "or",
    "pass",
    "print",
    "public",
    "raise",
    "readonly",
    "return",
    "short",
    "signed",
    "sizeof",
    "struct",
    "try",
    "typeid",
    "union",
    "unsigned",
    "while",
    "with",
    "yield",
]


C_keywords = [
    "auto",
    "break",
    " case",
    "char",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extern",
    "float",
    "for goto",
    "if",
    "int",
    "long",
    "register",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "typedef",
    "union",
    "unsigned",
    "void",
    "volatile",
    "while",
]


# Exlude C keywords. Some of them are valid type identifiers, other will have been
# disallowed by the C preprocessor in any case so they won't get to us:
keywords = set(cython_keywords) - set(C_keywords)
