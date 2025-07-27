rule auto_rule_20250726074031_0823 {
  strings:
    $o0 = "xF89C853F" wide ascii nocase
    $o1 = "x3614u" wide ascii nocase
    $o2 = "xF89C8533" wide ascii nocase
  condition:
    3 of ($o*)
}