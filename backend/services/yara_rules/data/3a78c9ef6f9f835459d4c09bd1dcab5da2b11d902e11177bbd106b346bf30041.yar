rule auto_rule_20250726104519_7311 {
  strings:
    $o0 = "dword_45CDBC" wide ascii nocase
  condition:
    all of them
}