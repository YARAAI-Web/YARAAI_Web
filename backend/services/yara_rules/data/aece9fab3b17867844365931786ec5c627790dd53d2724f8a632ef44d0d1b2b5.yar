rule auto_rule_20250727011105_2813 {
  strings:
    $o0 = "dword_47722C" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
  condition:
    all of them
}