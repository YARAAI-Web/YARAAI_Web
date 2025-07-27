rule auto_rule_20250727015843_8055 {
  strings:
    $o0 = "__endstdio" wide ascii nocase
    $o1 = "dword_4672B0" wide ascii nocase
    $o2 = "_heap_alloc_base" wide ascii nocase
  condition:
    3 of ($o*)
}