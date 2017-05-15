# -*- coding: utf-8 -*-
import os
import zipfile

import pytest

from cihai.bootstrap import UNIHAN_FILES
from cihai.core import Cihai


@pytest.fixture
def fixture_path():
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'fixtures',
    ))


@pytest.fixture
def test_config_file(fixture_path):
    return os.path.join(
        fixture_path,
        'test_config.yml'
    )


@pytest.fixture
def cihai_obj(test_config_file):
    return Cihai.from_file(test_config_file)


@pytest.fixture
def zip_path(tmpdir):
    return tmpdir.join('Unihan.zip')


@pytest.fixture
def zip_file(zip_path, fixture_path):
    _files = []
    for f in UNIHAN_FILES:
        _files += [os.path.join(
            fixture_path, f
        )]
    print(_files)
    zf = zipfile.ZipFile(str(zip_path), 'a')
    for f in _files:
        print(f)
        zf.write(f, os.path.basename(f))
    zf.close()
    return zf


@pytest.fixture
def unihan_options(zip_file, zip_path, tmpdir):
    return {
        'source': str(zip_path),
        'work_dir': str(tmpdir),
        'zip_path': str(tmpdir.join('downloads').join('Moo.zip'))
    }