rule auto_rule_20250726214255_9442 {
  strings:
    $o0 = "GetStringTypeA" wide ascii nocase
    $o1 = "off_45C914" wide ascii nocase
    $o2 = "main_loop_0" wide ascii nocase
    $o3 = "_byte_0" wide ascii nocase
  condition:
    4 of ($o*)
}