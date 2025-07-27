rule auto_rule_20250726104758_0741 {
  strings:
    $o0 = "main_loop_entrance_0" wide ascii nocase
    $o1 = "dword_456D34" wide ascii nocase
  condition:
    all of them
}