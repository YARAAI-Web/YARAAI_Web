rule auto_rule_20250726114243_1943 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "dword_449AD8" wide ascii nocase
    $o2 = "TrailDown2" wide ascii nocase
    $o3 = "doexit" wide ascii nocase
  condition:
    4 of ($o*)
}