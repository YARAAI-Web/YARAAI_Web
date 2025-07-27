rule auto_rule_20250726170138_2140 {
  strings:
    $o0 = "dword_44A3A4" wide ascii nocase
  condition:
    all of them
}