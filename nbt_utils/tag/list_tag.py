r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
 
 Copyright 2021 Podrum Team.
 
 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

from nbt_utils.tag_identifiers import TagIdentifiers
from nbt_utils.utils.nbt import Nbt


class ListTag:
    def __init__(self, name: str = "", value: list = [], list_type: int = 1):
        self.id: int = TagIdentifiers.LIST_TAG
        self.name: str = name
        self.value: list = value
        self.list_type: int = list_type
        
    def read(self, stream) -> None:
        self.list_type = stream.read_byte_tag()
        size: int = stream.read_int_tag()
        result: list = []
        for i in range(0, size):
            tag = Nbt.new_tag(self.list_type)
            tag.read(stream)
            result.append(tag)
        self.value = result
        
    def write(self, stream) -> None:
        stream.write_byte_tag(self.list_type)
        stream.write_int_tag(len(self.value))
        for item in self.value:
            item.write(stream)
