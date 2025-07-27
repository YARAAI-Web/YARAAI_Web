rule auto_rule_20250726075210_9767 {
  strings:
    $o0 = "_abstract_cw" wide ascii nocase
    $o1 = "x41C4u" wide ascii nocase
    $o2 = "main_loop_start" wide ascii nocase
  condition:
    3 of ($o*)
}