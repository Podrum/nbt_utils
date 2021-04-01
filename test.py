from nbt_utils.utils.nbt_be_binary_stream import nbt_be_binary_stream
from nbt_utils.tag.compound_tag import compound_tag
import os

file_dir: str = os.path.abspath(os.path.dirname(__file__))
file: object = open(file_dir + "/hello_world.nbt", "rb")
stream: object = nbt_be_binary_stream(file.read())
tag: object = compound_tag()
tag.read(stream)
print(tag.get_tag("hello world").get_tag("name").value)
