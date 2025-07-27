rule auto_rule_20250726162659_4631 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "_cpinfo" wide ascii nocase
    $o2 = "__crtMessageBoxA" wide ascii nocase
    $o3 = "byte_44A080" wide ascii nocase
  condition:
    4 of ($o*)
}