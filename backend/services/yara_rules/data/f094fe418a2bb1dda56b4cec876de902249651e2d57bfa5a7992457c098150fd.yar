rule auto_rule_20250726144917_3401 {
  strings:
    $o0 = "_heap_init" wide ascii nocase
    $o1 = "dword_44A3B8" wide ascii nocase
    $o2 = "program" wide ascii nocase
  condition:
    3 of ($o*)
}