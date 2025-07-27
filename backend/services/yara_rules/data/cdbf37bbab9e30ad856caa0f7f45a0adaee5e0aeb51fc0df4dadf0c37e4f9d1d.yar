rule auto_rule_20250726080331_8042 {
  strings:
    $o0 = "StringTypeW" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_4568D8" wide ascii nocase
    $o3 = "_cropzeros" wide ascii nocase
    $o4 = "x80000u" wide ascii nocase
  condition:
    5 of ($o*)
}