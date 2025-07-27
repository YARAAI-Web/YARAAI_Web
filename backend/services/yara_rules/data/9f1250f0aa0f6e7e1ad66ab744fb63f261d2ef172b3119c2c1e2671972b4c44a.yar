rule auto_rule_20250726170848_6230 {
  strings:
    $o0 = "flAllocationType" wide ascii nocase
    $o1 = "x17000u" wide ascii nocase
  condition:
    all of them
}