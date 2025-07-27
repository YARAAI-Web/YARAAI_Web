rule auto_rule_20250727033201_5919 {
  strings:
    $o0 = "dword_45D558" wide ascii nocase
    $o1 = "dword_45D7A0" wide ascii nocase
    $o2 = "__sbh_heap_init" wide ascii nocase
    $o3 = "TrailUp0_0" wide ascii nocase
    $o4 = "__crtMessageBoxA" wide ascii nocase
  condition:
    4 of ($o*)
}