rule auto_rule_20250726195533_5629 {
  strings:
    $o0 = "dword_411E54" wide ascii nocase
    $o1 = "dword_411F90" wide ascii nocase
    $o2 = "_cpinfo" wide ascii nocase
  condition:
    3 of ($o*)
}