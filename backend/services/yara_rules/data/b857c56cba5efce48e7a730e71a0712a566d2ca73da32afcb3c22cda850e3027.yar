rule auto_rule_20250726212900_8704 {
  strings:
    $o0 = "dword_78B04" wide ascii nocase
  condition:
    all of them
}