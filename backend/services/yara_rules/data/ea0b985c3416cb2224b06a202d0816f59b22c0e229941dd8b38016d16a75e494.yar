rule auto_rule_20250726195510_5316 {
  strings:
    $o0 = "dword_41B700" wide ascii nocase
  condition:
    all of them
}