rule auto_rule_20250726192326_5163 {
  strings:
    $o0 = "_heap_init" wide ascii nocase
    $o1 = "dword_45CAD8" wide ascii nocase
    $o2 = "_cpinfo" wide ascii nocase
    $o3 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}