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

from binary_utils.binary_stream import BinaryStream
from nbt_utils.tag.end_tag import EndTag
from nbt_utils.utils.nbt import Nbt


class NbtLeBinaryStream(BinaryStream):
    def read_byte_tag(self) -> int:
        return self.read_byte()
      
    def write_byte_tag(self, value: int) -> None:
        self.write_byte(value)
        
    def read_short_tag(self) -> int:
        return self.read_short_le()
      
    def write_short_tag(self, value: int) -> None:
        self.write_short_le(value)
        
    def read_int_tag(self) -> int:
        return self.read_int_le()
      
    def write_int_tag(self, value: int) -> None:
        self.write_int_le(value)
        
    def read_long_tag(self) -> int:
        return self.read_long_le()
      
    def write_long_tag(self, value: int) -> None:
        self.write_long_le(value)
        
    def read_float_tag(self) -> float:
        return self.read_float_le()
      
    def write_float_tag(self, value: float) -> None:
        self.write_float_le(value)
        
    def read_double_tag(self) -> float:
        return self.read_double_le()
      
    def write_double_tag(self, value: float) -> None:
        self.write_double_le(value)
            
    def read_string_tag(self) -> str:
        return self.read(self.read_unsigned_short_le()).decode()
      
    def write_string_tag(self, value: str) -> None:
        self.write_unsigned_short_le(len(value))
        self.write(value.encode())

    def read_root_tag(self):
        if not self.feos():
            new_tag = Nbt.new_tag(self.read_byte_tag())
            if not isinstance(new_tag, EndTag):
                new_tag.name = self.read_string_tag()
                new_tag.read(self)
            return new_tag

    def write_root_tag(self, value) -> None:
        self.write_byte_tag(value.id)
        if not isinstance(value, EndTag):
            self.write_string_tag(value.name)
            value.write(self)
