rule auto_rule_20250726082402_7736 {
  strings:
    $o0 = "_heap_init" wide ascii nocase
    $o1 = "off_45C91C" wide ascii nocase
    $o2 = "_getptd" wide ascii nocase
    $o3 = "tail_loop_start" wide ascii nocase
  condition:
    4 of ($o*)
}