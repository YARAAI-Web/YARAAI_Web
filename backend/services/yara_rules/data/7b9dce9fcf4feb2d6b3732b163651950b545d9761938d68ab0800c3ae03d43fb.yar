rule auto_rule_20250726105715_5194 {
  strings:
    $o0 = "__initstdio" wide ascii nocase
    $o1 = "byte_463AE4" wide ascii nocase
    $o2 = "start_byte_3" wide ascii nocase
    $o3 = "xC000008F" wide ascii nocase
  condition:
    4 of ($o*)
}