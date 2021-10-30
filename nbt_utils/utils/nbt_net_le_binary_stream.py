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

from nbt_utils.utils.nbt_le_binary_stream import NbtLeBinaryStream


class NbtNetLeBinaryStream(NbtLeBinaryStream):
    def read_int_tag(self) -> int:
        return self.read_signed_var_int()
      
    def write_int_tag(self, value: int) -> None:
        self.write_signed_var_int(value)
        
    def read_long_tag(self) -> int:
        return self.read_signed_var_long()
      
    def write_long_tag(self, value: int) -> None:
        self.write_signed_var_long(value)
        
    def read_string_tag(self) -> str:
        return self.read(self.read_var_int()).decode()
      
    def write_string_tag(self, value: str) -> None:
        self.write_var_int(len(value))
        self.write(value.encode())
            
