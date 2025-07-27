rule auto_rule_20250726181706_7844 {
  strings:
    $o0 = "algn_476BF2" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
    $o2 = "dodwords" wide ascii nocase
  condition:
    3 of ($o*)
}