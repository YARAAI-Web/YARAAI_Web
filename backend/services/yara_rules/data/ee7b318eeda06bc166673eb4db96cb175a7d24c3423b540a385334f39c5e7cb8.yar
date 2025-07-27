rule auto_rule_20250726134116_1025 {
  strings:
    $o0 = "aStftware" wide ascii nocase
    $o1 = "flAllocationType" wide ascii nocase
  condition:
    all of them
}