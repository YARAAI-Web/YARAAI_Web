rule auto_rule_20250726145858_2946 {
  strings:
    $o0 = "dword_4C1684" wide ascii nocase
  condition:
    all of them
}