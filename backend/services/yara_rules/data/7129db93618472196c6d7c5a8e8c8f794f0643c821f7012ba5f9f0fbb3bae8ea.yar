rule auto_rule_20250726143051_1678 {
  strings:
    $o0 = "SourceString" wide ascii nocase
    $o1 = "x4221F5" wide ascii nocase
    $o2 = "C25h" wide ascii nocase
    $o3 = "off_422738" wide ascii nocase
  condition:
    4 of ($o*)
}