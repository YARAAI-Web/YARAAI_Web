rule auto_rule_20250726125325_8719 {
  strings:
    $o0 = "_except_handler3" wide ascii nocase
    $o1 = "dword_411170" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
  condition:
    3 of ($o*)
}