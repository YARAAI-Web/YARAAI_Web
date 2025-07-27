rule auto_rule_20250726133654_9617 {
  strings:
    $o0 = "_aullrem" wide ascii nocase
    $o1 = "dword_467B70" wide ascii nocase
  condition:
    all of them
}