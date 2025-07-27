rule auto_rule_20250726080449_7381 {
  strings:
    $o0 = "__sbh_heap_init" wide ascii nocase
    $o1 = "dword_45CF04" wide ascii nocase
    $o2 = "_enable" wide ascii nocase
    $o3 = "dword_428EF8" wide ascii nocase
  condition:
    4 of ($o*)
}