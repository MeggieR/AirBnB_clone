#!/usr/bin/python3
"""connects storage to basemodel"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
