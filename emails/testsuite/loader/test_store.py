# encoding: utf-8
from __future__ import unicode_literals
import emails


def test_lazy_http():
    IMG_URL = 'http://lavr.github.io/python-emails/tests/python-logo.gif'
    f = emails.store.LazyHTTPFile(uri=IMG_URL)
    assert f.filename == 'python-logo.gif'
    assert f.content_disposition is None
    assert len(f.data) == 2549


def test_store_commons():
    FILES = [{'data': 'aaa', 'filename': 'aaa.txt'}, {'data': 'bbb', 'filename': 'bbb.txt'}, ]
    store = emails.store.MemoryFileStore()
    [store.add(_) for _ in FILES]
    for i, stored_file in enumerate(store):
        orig_file = FILES[i]
        for (k, v) in orig_file.items():
            assert v == getattr(stored_file, k)

