rule auto_rule_20250726080129_7708 {
  strings:
    $o0 = "dword_4762F4" wide ascii nocase
  condition:
    all of them
}