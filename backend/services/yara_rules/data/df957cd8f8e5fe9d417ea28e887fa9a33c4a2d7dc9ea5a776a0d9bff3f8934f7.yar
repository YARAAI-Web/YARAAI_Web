rule auto_rule_20250726170520_1771 {
  strings:
    $o0 = "F28h" wide ascii nocase
    $o1 = "byte_640265FE" wide ascii nocase
    $o2 = "ResourceW" wide ascii nocase
  condition:
    3 of ($o*)
}