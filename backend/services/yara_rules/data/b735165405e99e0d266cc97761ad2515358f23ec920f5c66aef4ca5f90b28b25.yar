rule auto_rule_20250727013845_9791 {
  strings:
    $o0 = "dword_479960" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    all of them
}