# -*- coding: utf-8 -*-

import hashlib


class MD5(object):

    def __repr__(self):
        return '<MD5>'

    @classmethod
    def hexdigest(cls, obj):
        digest = hashlib.md5()

        if isinstance(obj, (str, int)):
            digest.update(obj.__class__.__name__.encode('utf-8'))
            digest.update(('%s' % obj).encode('utf-8'))

        elif isinstance(obj, bool) or obj is None:
            digest.update(obj.__class__.__name__.encode('utf-8'))

        elif isinstance(obj, (list, tuple)):
            digest.update(obj.__class__.__name__.encode('utf-8'))
            for e in obj:
                digest.update(cls.hexdigest(e).encode('utf-8'))

        elif isinstance(obj, dict):
            digest.update(obj.__class__.__name__.encode('utf-8'))
            hexs = [cls.hexdigest([k, v]) for k, v in obj.items()]
            hexs.sort()
            for e in hexs:
                digest.update(e.encode('utf-8'))

        else:
            raise TypeError("can't convert %s into String" % obj)

        return digest.hexdigest()
