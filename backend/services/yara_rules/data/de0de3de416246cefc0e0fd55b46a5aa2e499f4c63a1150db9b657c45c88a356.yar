rule auto_rule_20250726204702_3425 {
  strings:
    $o0 = "dword_42E6D5" wide ascii nocase
    $o1 = "dword_42E739" wide ascii nocase
    $o2 = "dword_42E8C1" wide ascii nocase
    $o3 = "x75FDu" wide ascii nocase
    $o4 = "dword_42D020" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726204706_0953 {
  strings:
    $o0 = "IncrementDataOld" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726204709_4002 {
  condition:
    auto_rule_20250726204702_3425 or auto_rule_20250726204706_0953
}