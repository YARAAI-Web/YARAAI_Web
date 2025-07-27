rule auto_rule_20250726112200_5990 {
  strings:
    $o0 = "dword_45CEF8" wide ascii nocase
  condition:
    all of them
}