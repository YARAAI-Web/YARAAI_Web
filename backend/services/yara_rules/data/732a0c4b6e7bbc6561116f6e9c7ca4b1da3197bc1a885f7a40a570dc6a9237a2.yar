rule auto_rule_20250726233036_7942 {
  strings:
    $o0 = "dword_4431CC" wide ascii nocase
  condition:
    all of them
}