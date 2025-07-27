rule auto_rule_20250726115009_7314 {
  strings:
    $o0 = "dword_42E890" wide ascii nocase
    $o1 = "_getptd" wide ascii nocase
    $o2 = "__sbh_alloc_new_group" wide ascii nocase
    $o3 = "program" wide ascii nocase
  condition:
    4 of ($o*)
}