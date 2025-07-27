rule auto_rule_20250726104541_8108 {
  strings:
    $o0 = "nBlockUse" wide ascii nocase
    $o1 = "TrailUp3" wide ascii nocase
    $o2 = "__sbh_alloc_new_group" wide ascii nocase
    $o3 = "byte_40DBF8" wide ascii nocase
  condition:
    4 of ($o*)
}