rule auto_rule_20250726223637_0477 {
  strings:
    $o0 = "MapVirtualKeyA" wide ascii nocase
    $o1 = "cchMaxCount" wide ascii nocase
  condition:
    all of them
}