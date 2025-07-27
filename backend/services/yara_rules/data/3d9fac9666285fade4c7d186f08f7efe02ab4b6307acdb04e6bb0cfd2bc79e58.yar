rule auto_rule_20250727004230_5761 {
  strings:
    $o0 = "x402044" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    all of them
}