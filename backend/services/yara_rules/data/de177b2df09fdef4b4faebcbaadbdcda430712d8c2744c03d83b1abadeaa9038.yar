rule auto_rule_20250726153314_6270 {
  strings:
    $o0 = "dword_4673BC" wide ascii nocase
  condition:
    all of them
}