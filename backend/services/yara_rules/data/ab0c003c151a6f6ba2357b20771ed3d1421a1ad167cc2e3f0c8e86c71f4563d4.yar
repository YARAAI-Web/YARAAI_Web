rule auto_rule_20250727002413_3361 {
  strings:
    $o0 = "__sbh_alloc_new_region" wide ascii nocase
    $o1 = "dword_4765C8" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "_cpinfo" wide ascii nocase
    $o4 = "dword_477544" wide ascii nocase
  condition:
    4 of ($o*)
}