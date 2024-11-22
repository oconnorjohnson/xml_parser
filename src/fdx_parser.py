from pathlib import Path
from lxml import etree
from typing import List, Dict, Union

class FDXParser:
    def __init__(self):
        self.tree = None
        self.root = None
        
    def load_file(self, file_path: Union[str, Path]) -> bool:
        """Load and parse an FDX file."""
        try:
            self.tree = etree.parse(str(file_path))
            self.root = self.tree.getroot()
            return True
        except (etree.ParseError, IOError):
            return False
            
    def parse(self) -> List[Dict[str, str]]:
        """Parse the FDX file and return a list of screenplay elements."""
        if self.root is None:
            return []
            
        elements = []
        
        # Find all Paragraph elements
        for paragraph in self.root.findall(".//Paragraph"):
            element_type = paragraph.get("Type", "").lower()
            text_element = paragraph.find("Text")
            content = text_element.text if text_element is not None else ""
            
            # Map FDX types to our internal types
            type_mapping = {
                "scene heading": "scene_heading",
                "action": "action",
                "character": "character",
                "dialogue": "dialogue",
                # Add more mappings as needed
            }
            
            elements.append({
                "type": type_mapping.get(element_type, element_type),
                "content": content
            })
            
        return elements
