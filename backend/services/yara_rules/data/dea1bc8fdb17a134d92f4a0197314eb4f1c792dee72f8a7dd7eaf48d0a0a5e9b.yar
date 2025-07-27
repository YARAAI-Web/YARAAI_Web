rule auto_rule_20250726095957_1531 {
  strings:
    $o0 = "dword_459030" wide ascii nocase
  condition:
    all of them
}