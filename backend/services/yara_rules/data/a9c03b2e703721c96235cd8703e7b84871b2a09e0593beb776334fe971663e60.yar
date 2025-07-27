rule auto_rule_20250726145106_8808 {
  strings:
    $o0 = "aClasses" wide ascii nocase
    $o1 = "flAllocationType" wide ascii nocase
  condition:
    all of them
}