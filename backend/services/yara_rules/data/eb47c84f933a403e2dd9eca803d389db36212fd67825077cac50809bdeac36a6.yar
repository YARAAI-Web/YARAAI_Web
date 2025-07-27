rule auto_rule_20250726144936_9367 {
  strings:
    $o0 = "dword_78308" wide ascii nocase
    $o1 = "dword_77728" wide ascii nocase
  condition:
    all of them
}