rule auto_rule_20250726230728_9907 {
  strings:
    $o0 = "dword_78514" wide ascii nocase
  condition:
    all of them
}