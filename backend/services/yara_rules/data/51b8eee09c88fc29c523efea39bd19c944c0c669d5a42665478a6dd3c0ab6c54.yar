rule auto_rule_20250727001251_2138 {
  strings:
    $o0 = "tail_loop_start" wide ascii nocase
    $o1 = "byte_45D580" wide ascii nocase
  condition:
    all of them
}