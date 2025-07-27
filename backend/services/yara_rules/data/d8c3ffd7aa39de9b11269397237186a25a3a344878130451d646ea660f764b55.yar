rule auto_rule_20250726145958_5488 {
  strings:
    $o0 = "dword_423700" wide ascii nocase
    $o1 = "dword_42A268" wide ascii nocase
  condition:
    all of them
}