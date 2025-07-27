rule auto_rule_20250726141131_0152 {
  strings:
    $o0 = "dword_4164C4" wide ascii nocase
    $o1 = "aMqa44e2xIb" wide ascii nocase
    $o2 = "stru_414014" wide ascii nocase
    $o3 = "x58A1u" wide ascii nocase
    $o4 = "dwMemoryLoad" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726141135_0132 {
  strings:
    $o0 = "dword_413C02" wide ascii nocase
    $o1 = "aLsqPq8Fqj32" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726141140_5107 {
  condition:
    auto_rule_20250726141131_0152 or auto_rule_20250726141135_0132
}