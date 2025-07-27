rule auto_rule_20250726104633_4678 {
  strings:
    $o0 = "x900405C" wide ascii nocase
    $o1 = "x9004058" wide ascii nocase
    $o2 = "xFFFEFFFF" wide ascii nocase
  condition:
    3 of ($o*)
}