rule auto_rule_20250726195931_2741 {
  strings:
    $o0 = "dword_14008D490" wide ascii nocase
  condition:
    all of them
}