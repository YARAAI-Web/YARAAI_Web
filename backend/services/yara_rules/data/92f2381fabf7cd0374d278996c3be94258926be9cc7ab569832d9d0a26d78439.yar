rule auto_rule_20250726112351_4272 {
  strings:
    $o0 = "dword_6402E168" wide ascii nocase
  condition:
    all of them
}