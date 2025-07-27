rule auto_rule_20250726212911_1300 {
  strings:
    $o0 = "byte_6402E068" wide ascii nocase
  condition:
    all of them
}