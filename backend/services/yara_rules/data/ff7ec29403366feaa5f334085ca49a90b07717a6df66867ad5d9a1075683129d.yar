rule auto_rule_20250727042135_1929 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "Handler" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "dword_4626D4" wide ascii nocase
  condition:
    4 of ($o*)
}