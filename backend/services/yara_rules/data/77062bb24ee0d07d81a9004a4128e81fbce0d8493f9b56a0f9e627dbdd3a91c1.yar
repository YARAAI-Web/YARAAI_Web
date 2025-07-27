rule auto_rule_20250726134715_0185 {
  strings:
    $o0 = "GetActiveWindow_0" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
    $o2 = "byte_45D3EC" wide ascii nocase
  condition:
    3 of ($o*)
}