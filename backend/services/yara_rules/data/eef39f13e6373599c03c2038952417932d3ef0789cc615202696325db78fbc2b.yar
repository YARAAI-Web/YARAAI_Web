rule auto_rule_20250726145620_5051 {
  strings:
    $o0 = "located" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "byte_460DD8" wide ascii nocase
  condition:
    3 of ($o*)
}