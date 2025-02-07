import json
from lxml import etree
import xml.etree.ElementTree as ET
import os
import glob

PATH_TO_DATA = ""
PATH_TO_CONFIG = "./config.json"

config = json.load(open(PATH_TO_CONFIG))
rel_classes = config["relevant_classes"]

for file in glob.iglob(f"{os.path.join(PATH_TO_DATA, "annotations")}/*.xml"):
  tree = etree.fromstring(open(file).read())

  for object in tree.xpath("//object"):
    if object.findtext("name") not in rel_classes:
      object.getparent().remove(object)

  ET.ElementTree(tree).write(file)
