rule auto_rule_20250726060136_3611 {
  strings:
    $o0 = "nFile" wide ascii nocase
    $o1 = "dword_467EB4" wide ascii nocase
  condition:
    all of them
}