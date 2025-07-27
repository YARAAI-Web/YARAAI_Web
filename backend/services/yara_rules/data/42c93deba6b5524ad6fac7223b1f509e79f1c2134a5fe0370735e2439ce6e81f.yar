rule auto_rule_20250726170400_9257 {
  strings:
    $o0 = "lpszNewItem" wide ascii nocase
    $o1 = "wCmd" wide ascii nocase
  condition:
    all of them
}