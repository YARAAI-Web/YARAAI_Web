rule auto_rule_20250726160949_7869 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "off_74976C" wide ascii nocase
  condition:
    all of them
}