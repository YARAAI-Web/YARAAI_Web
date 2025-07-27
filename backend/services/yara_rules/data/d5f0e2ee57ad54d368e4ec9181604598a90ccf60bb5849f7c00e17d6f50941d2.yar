rule auto_rule_20250726124416_9216 {
  strings:
    $o0 = "dword_4695E8" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
    $o2 = "dword_469548" wide ascii nocase
  condition:
    3 of ($o*)
}