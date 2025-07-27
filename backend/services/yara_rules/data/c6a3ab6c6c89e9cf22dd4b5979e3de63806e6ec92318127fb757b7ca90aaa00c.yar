rule auto_rule_20250726184530_6121 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "xFF000000" wide ascii nocase
    $o2 = "dword_44C62C" wide ascii nocase
  condition:
    3 of ($o*)
}