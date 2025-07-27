rule auto_rule_20250726062604_9641 {
  strings:
    $o0 = "xB77" wide ascii nocase
    $o1 = "dword_413C1A" wide ascii nocase
    $o2 = "DefaultChar" wide ascii nocase
    $o3 = "EnumResourceTypesA" wide ascii nocase
    $o4 = "x752E" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726062607_3608 {
  strings:
    $o0 = "xF89F85B0" wide ascii nocase
    $o1 = "dword_413C0E" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726062612_0520 {
  condition:
    auto_rule_20250726062604_9641 or auto_rule_20250726062607_3608
}