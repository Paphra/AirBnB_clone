#!/usr/bin/python3
"""The models package
"""

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
