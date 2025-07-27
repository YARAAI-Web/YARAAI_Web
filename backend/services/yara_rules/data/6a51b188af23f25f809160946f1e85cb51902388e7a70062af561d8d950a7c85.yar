rule auto_rule_20250726234607_6944 {
  strings:
    $o0 = "dword_467280" wide ascii nocase
  condition:
    all of them
}