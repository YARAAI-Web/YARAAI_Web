rule auto_rule_20250726164418_9372 {
  strings:
    $o0 = "fill_dwords_with_EOS" wide ascii nocase
    $o1 = "tail_loop_start" wide ascii nocase
    $o2 = "off_478C7C" wide ascii nocase
    $o3 = "main_loop_0" wide ascii nocase
  condition:
    4 of ($o*)
}