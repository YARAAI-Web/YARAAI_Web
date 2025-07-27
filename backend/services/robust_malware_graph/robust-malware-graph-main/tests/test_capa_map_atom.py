import pytest

from src.rulegen.capa_builder import _map_atom_to_feature

@pytest.mark.parametrize(
    "atom,expected",
    [
        ("path:C\\Windows", ("string", "C\\Windows")),
        ("reg:HKLM\\Software", ("string", "HKLM\\Software")),
        ("url:http://example.com", ("string", "http://example.com")),
    ],
)
def test_path_reg_url_mapped_to_string(atom, expected):
    assert _map_atom_to_feature(atom) == expected
