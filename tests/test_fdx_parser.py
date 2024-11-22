import pytest
from pathlib import Path
from src.fdx_parser import FDXParser

# Sample FDX content for testing
SAMPLE_FDX = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<FinalDraft DocumentType="Script">
    <Content>
        <Paragraph Type="Scene Heading">
            <Text>INT. ROOM - DAY</Text>
        </Paragraph>
        <Paragraph Type="Action">
            <Text>A computer sits on a desk, displaying code.</Text>
        </Paragraph>
        <Paragraph Type="Character">
            <Text>PROGRAMMER</Text>
        </Paragraph>
        <Paragraph Type="Dialogue">
            <Text>This better work.</Text>
        </Paragraph>
    </Content>
</FinalDraft>'''

@pytest.fixture
def sample_fdx_file(tmp_path):
    fdx_file = tmp_path / "sample.fdx"
    fdx_file.write_text(SAMPLE_FDX)
    return fdx_file

def test_fdx_parser_initialization():
    parser = FDXParser()
    assert parser is not None

def test_can_load_fdx_file(sample_fdx_file):
    parser = FDXParser()
    result = parser.load_file(sample_fdx_file)
    assert result is True

def test_parse_scene_heading(sample_fdx_file):
    parser = FDXParser()
    parser.load_file(sample_fdx_file)
    elements = parser.parse()
    assert elements[0]["type"] == "scene_heading"
    assert elements[0]["content"] == "INT. ROOM - DAY"

def test_parse_action(sample_fdx_file):
    parser = FDXParser()
    parser.load_file(sample_fdx_file)
    elements = parser.parse()
    assert elements[1]["type"] == "action"
    assert elements[1]["content"] == "A computer sits on a desk, displaying code."

def test_parse_character(sample_fdx_file):
    parser = FDXParser()
    parser.load_file(sample_fdx_file)
    elements = parser.parse()
    assert elements[2]["type"] == "character"
    assert elements[2]["content"] == "PROGRAMMER"

def test_parse_dialogue(sample_fdx_file):
    parser = FDXParser()
    parser.load_file(sample_fdx_file)
    elements = parser.parse()
    assert elements[3]["type"] == "dialogue"
    assert elements[3]["content"] == "This better work."
