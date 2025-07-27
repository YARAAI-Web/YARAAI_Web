rule auto_rule_20250726225401_3615 {
  strings:
    $o0 = "dword_457010" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "xFFF7FFFF" wide ascii nocase
  condition:
    3 of ($o*)
}