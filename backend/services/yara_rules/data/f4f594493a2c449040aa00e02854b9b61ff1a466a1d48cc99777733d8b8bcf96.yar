rule auto_rule_20250726065004_0058 {
  strings:
    $o0 = "off_4B26C4" wide ascii nocase
    $o1 = "dword_4C2190" wide ascii nocase
  condition:
    all of them
}