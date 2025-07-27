rule auto_rule_20250726155234_2983 {
  strings:
    $o0 = "_setenvp" wide ascii nocase
    $o1 = "dword_45FD84" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
  condition:
    3 of ($o*)
}