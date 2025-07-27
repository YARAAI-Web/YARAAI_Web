rule auto_rule_20250726155745_6149 {
  strings:
    $o0 = "_setenvp" wide ascii nocase
    $o1 = "_c_exit" wide ascii nocase
    $o2 = "_heap_init" wide ascii nocase
    $o3 = "TrailDown2" wide ascii nocase
    $o4 = "dword_477668" wide ascii nocase
  condition:
    5 of ($o*)
}