rule auto_rule_20250726192841_8071 {
  strings:
    $o0 = "dword_44C3D4" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
    $o2 = "dword_44C7B8" wide ascii nocase
  condition:
    3 of ($o*)
}