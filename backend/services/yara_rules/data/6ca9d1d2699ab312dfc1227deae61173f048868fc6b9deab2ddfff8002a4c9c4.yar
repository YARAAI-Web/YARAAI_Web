rule auto_rule_20250726234240_2079 {
  strings:
    $o0 = "dword_44A03C" wide ascii nocase
    $o1 = "x_ismbbtype" wide ascii nocase
    $o2 = "LoadCursorA" wide ascii nocase
    $o3 = "dword_449EF4" wide ascii nocase
    $o4 = "__sbh_alloc_new_group" wide ascii nocase
  condition:
    4 of ($o*)
}