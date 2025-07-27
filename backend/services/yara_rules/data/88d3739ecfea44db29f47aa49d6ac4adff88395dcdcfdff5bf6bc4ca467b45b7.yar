rule auto_rule_20250726133310_3203 {
  strings:
    $o0 = "xFFFEFFFF" wide ascii nocase
    $o1 = "dword_780FC" wide ascii nocase
  condition:
    all of them
}