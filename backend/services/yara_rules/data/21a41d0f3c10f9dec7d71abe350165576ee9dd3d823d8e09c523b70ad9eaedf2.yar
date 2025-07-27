rule auto_rule_20250726224125_0368 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "dword_4279C8" wide ascii nocase
    $o2 = "dword_427D00" wide ascii nocase
  condition:
    3 of ($o*)
}