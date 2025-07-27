rule auto_rule_20250727000518_5237 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "x413535" wide ascii nocase
    $o2 = "dword_447064" wide ascii nocase
  condition:
    3 of ($o*)
}