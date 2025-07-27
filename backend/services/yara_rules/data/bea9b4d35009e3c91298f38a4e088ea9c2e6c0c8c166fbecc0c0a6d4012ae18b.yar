rule auto_rule_20250726075310_0534 {
  strings:
    $o0 = "main_loop_1" wide ascii nocase
    $o1 = "dword_418008" wide ascii nocase
    $o2 = "dword_450568" wide ascii nocase
  condition:
    3 of ($o*)
}