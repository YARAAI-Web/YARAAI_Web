rule auto_rule_20250726162328_6251 {
  strings:
    $o0 = "__heap_select" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "x12010u" wide ascii nocase
    $o3 = "strcat" wide ascii nocase
    $o4 = "dword_45CAD4" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726162332_6349 {
  strings:
    $o0 = "dword_45D268" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726162343_1790 {
  condition:
    auto_rule_20250726162328_6251 or auto_rule_20250726162332_6349
}