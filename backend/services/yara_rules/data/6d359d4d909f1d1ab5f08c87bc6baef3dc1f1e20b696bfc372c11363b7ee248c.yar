rule auto_rule_20250726114135_9614 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "dword_463898" wide ascii nocase
  condition:
    all of them
}