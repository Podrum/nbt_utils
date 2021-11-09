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

from nbt_utils.tag.end_tag import EndTag
from nbt_utils.tag_identifiers import TagIdentifiers
from nbt_utils.utils.nbt import Nbt


class CompoundTag:
    def __init__(self, name: str = "", value: list = []):
        self.id: int = TagIdentifiers.COMPOUND_TAG
        self.name: str = name
        self.value: list = value
        
    def read(self, stream) -> None:
        result = []
        while not stream.feos():
            new_tag = Nbt.new_tag(stream.read_byte_tag())
            if isinstance(new_tag, EndTag):
                break
            new_tag.name = stream.read_string_tag()
            new_tag.read(stream)
            result.append(new_tag)
        self.value = result
        
    def write(self, stream) -> None:
        for tag in self.value:
            if not isinstance(tag, EndTag):
                stream.write_byte_tag(tag.id)
                stream.write_string_tag(tag.name)
                tag.write(stream)
        stream.write_byte_tag(0)
        
    def get_tag(self, name: str):
        for tag in self.value:
            if name == tag.name:
                return tag
            
    def has_tag(self, name: str) -> bool:
        for tag in self.value:
            if name == tag.name:
                return True
        return False
         
    def set_tag(self, tag) -> None:
        for i, v in enumerate(self.value):
            if tag.name == v.name:
                self.value[i] = tag
                return
        self.value.append(tag)
