rule auto_rule_20250726223836_2185 {
  strings:
    $o0 = "dword_77FD0" wide ascii nocase
  condition:
    all of them
}