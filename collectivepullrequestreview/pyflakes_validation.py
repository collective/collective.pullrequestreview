# -*- coding: utf-8 -*-
import os


def getPythonFilenames(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.py'):
                yield os.path.join(dirpath, filename)


class PyflakesValidation(object):

    def __init__(self, request):
        self.request = request

    def validate(self, repository):
        import _ast
        checker = __import__('pyflakes.checker').checker
        count = 0
        for filename in getPythonFilenames(repository.path):
            codeString = file(filename, 'U').read() + '\n'
            tree = compile(codeString, filename, "exec", _ast.PyCF_ONLY_AST)
            w = checker.Checker(tree, filename)
            w.messages.sort(lambda a, b: cmp(a.lineno, b.lineno))
            count += 1
        print count
