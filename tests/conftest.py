import pytest
import tempfile
from pathlib import Path


@pytest.fixture
def temp_file():
    """Create a temporary file path for testing"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
        temp_path = f.name
    yield temp_path
    # Cleanup
    Path(temp_path).unlink(missing_ok=True)


@pytest.fixture
def complete_xml_path():
    """Path to the complete.xml test file"""
    return Path(__file__).parent / "resources" / "complete.xml"


@pytest.fixture
def incomplete_xml_path():
    """Path to the incomplete.xml test file"""
    return Path(__file__).parent / "resources" / "incomplete.xml"


@pytest.fixture
def mixed_xml_path():
    """Path to the mixed.xml test file"""
    return Path(__file__).parent / "resources" / "mixed.xml"


@pytest.fixture
def unicode_xml_path():
    """Path to the unicode.xml test file"""
    return Path(__file__).parent / "resources" / "unicode.xml"
