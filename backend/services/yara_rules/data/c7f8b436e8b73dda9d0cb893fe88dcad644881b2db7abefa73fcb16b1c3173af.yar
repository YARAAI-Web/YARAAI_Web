rule auto_rule_20250726085747_1627 {
  strings:
    $o0 = "finish_loop" wide ascii nocase
    $o1 = "TrailUp0_0" wide ascii nocase
    $o2 = "dword_411EB0" wide ascii nocase
    $o3 = "__sbh_alloc_new_group" wide ascii nocase
  condition:
    4 of ($o*)
}