rule auto_rule_20250726161532_2456 {
  strings:
    $o0 = "dword_781A4" wide ascii nocase
  condition:
    all of them
}