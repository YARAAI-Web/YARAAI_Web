rule auto_rule_20250726141942_8108 {
  strings:
    $o0 = "dword_4D3148" wide ascii nocase
  condition:
    all of them
}