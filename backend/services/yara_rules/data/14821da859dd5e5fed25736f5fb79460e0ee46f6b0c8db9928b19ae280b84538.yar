rule auto_rule_20250726154226_8035 {
  strings:
    $o0 = "__sbh_alloc_new_region" wide ascii nocase
    $o1 = "TrailUp0_0" wide ascii nocase
    $o2 = "_abnormal_termination" wide ascii nocase
    $o3 = "byte_45FE08" wide ascii nocase
  condition:
    4 of ($o*)
}