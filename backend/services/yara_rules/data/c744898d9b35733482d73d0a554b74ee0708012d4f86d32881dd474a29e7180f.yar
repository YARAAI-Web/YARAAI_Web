rule auto_rule_20250726134457_0602 {
  strings:
    $o0 = "aClsid" wide ascii nocase
    $o1 = "ITypeLib" wide ascii nocase
    $o2 = "ExtFloodFill" wide ascii nocase
    $o3 = "rop2" wide ascii nocase
    $o4 = "SafeArrayGetElement" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726134500_5890 {
  strings:
    $o0 = "nPairs" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726134504_2705 {
  condition:
    auto_rule_20250726134457_0602 or auto_rule_20250726134500_5890
}