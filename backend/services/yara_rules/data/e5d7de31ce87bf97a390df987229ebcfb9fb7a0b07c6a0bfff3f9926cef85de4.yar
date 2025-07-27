rule auto_rule_20250726090903_7770 {
  strings:
    $o0 = "_CrtDbgReport" wide ascii nocase
    $o1 = "tail_loop_start" wide ascii nocase
    $o2 = "off_463998" wide ascii nocase
    $o3 = "x12012u" wide ascii nocase
  condition:
    4 of ($o*)
}