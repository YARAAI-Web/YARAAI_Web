rule auto_rule_20250727023450_1102 {
  strings:
    $o0 = "_heap_alloc" wide ascii nocase
    $o1 = "phmx" wide ascii nocase
    $o2 = "dword_45FE08" wide ascii nocase
  condition:
    3 of ($o*)
}