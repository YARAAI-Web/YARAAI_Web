rule auto_rule_20250726173152_3154 {
  strings:
    $o0 = "dword_44E198" wide ascii nocase
  condition:
    all of them
}