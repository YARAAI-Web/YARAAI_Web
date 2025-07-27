rule auto_rule_20250726100935_2042 {
  strings:
    $o0 = "CreateHatchBrush" wide ascii nocase
    $o1 = "szNewItem" wide ascii nocase
    $o2 = "IsBadReadPtr" wide ascii nocase
    $o3 = "off_4336FB" wide ascii nocase
    $o4 = "cOrientation" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726100938_4670 {
  strings:
    $o0 = "dword_4337A7" wide ascii nocase
    $o1 = "x5F09u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726100942_3456 {
  condition:
    auto_rule_20250726100935_2042 or auto_rule_20250726100938_4670
}