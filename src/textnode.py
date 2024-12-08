from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT  = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    



def text_node_to_html_node(text_node):
    if text_node is None:
        raise Exception("Text_node is None")
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
        