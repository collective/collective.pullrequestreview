# -*- coding: utf-8 -*-
"""
collective.pullrequestreview

Licensed under the GPL license, see LICENCE.txt for more details.
"""
import os
from os.path import exists
from shutil import rmtree
import subprocess
from tempfile import mkdtemp, template

DEV_NULL = open('/dev/null', 'w')


class GitRepository(object):

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def merge(self, repository_url, branch='master'):
        os.chdir(self.path)
        subprocess.check_call(['git', 'remote', 'add', 'head', repository_url], stdout=DEV_NULL, stderr=DEV_NULL)
        subprocess.check_call(['git', 'fetch', 'head'], stdout=DEV_NULL, stderr=DEV_NULL)
        subprocess.check_call(['git', 'merge', 'head/%s' % branch], stdout=DEV_NULL, stderr=DEV_NULL)


class GitClone(object):

    def __init__(self, name, url, suffix="", prefix=template, dir=None):
        self.base_path = mkdtemp(suffix, prefix, dir)
        self.name = name
        self.path = os.path.join(self.base_path, self.name)
        self.url = url

    def __enter__(self):
        os.chdir(self.base_path)
        subprocess.check_call(['git', 'clone', self.url], stdout=DEV_NULL, stderr=DEV_NULL)
        return GitRepository(self.name, self.path)

    def cleanup(self):
        if exists(self.base_path):
            rmtree(self.base_path)

    def __exit__(self, exc, value, tb):
        self.cleanup()
