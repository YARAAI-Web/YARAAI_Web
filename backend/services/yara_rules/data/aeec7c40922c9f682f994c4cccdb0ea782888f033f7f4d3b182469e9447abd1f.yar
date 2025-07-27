rule auto_rule_20250726134320_6932 {
  strings:
    $o0 = "main_loop_entrance_0" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "dword_457E00" wide ascii nocase
    $o3 = "_nh_malloc" wide ascii nocase
  condition:
    4 of ($o*)
}