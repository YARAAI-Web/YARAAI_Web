rule auto_rule_20250726172907_8259 {
  strings:
    $o0 = "byte_4479E8" wide ascii nocase
    $o1 = "byte_4470A8" wide ascii nocase
    $o2 = "x7FF00000" wide ascii nocase
    $o3 = "x30000" wide ascii nocase
  condition:
    4 of ($o*)
}