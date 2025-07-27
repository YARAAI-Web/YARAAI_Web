rule auto_rule_20250726070933_8849 {
  strings:
    $o0 = "dword_6402D3D4" wide ascii nocase
    $o1 = "dword_6402B90C" wide ascii nocase
    $o2 = "dword_6402D32C" wide ascii nocase
  condition:
    3 of ($o*)
}