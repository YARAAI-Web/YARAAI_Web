rule auto_rule_20250726193805_4254 {
  strings:
    $o0 = "stdenvp" wide ascii nocase
    $o1 = "__sbh_alloc_block" wide ascii nocase
    $o2 = "TrailDown0" wide ascii nocase
    $o3 = "a_env" wide ascii nocase
    $o4 = "__sbh_alloc_new_group" wide ascii nocase
  condition:
    4 of ($o*)
}