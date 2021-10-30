from nbt_utils.utils.nbt_be_binary_stream import NbtBeBinaryStream
from nbt_utils.tag.compound_tag import CompoundTag
import os

file_dir: str = os.path.abspath(os.path.dirname(__file__))
file = open(file_dir + "/hello_world.nbt", "rb")
stream: NbtBeBinaryStream = NbtBeBinaryStream(file.read())
tag: CompoundTag = CompoundTag()
tag.read(stream)
print(tag.get_tag("hello world").get_tag("name").value)
