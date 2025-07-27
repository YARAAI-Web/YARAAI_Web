rule auto_rule_20250726175157_7896 {
  strings:
    $o0 = "off_47206C" wide ascii nocase
    $o1 = "strcspn" wide ascii nocase
    $o2 = "differ" wide ascii nocase
    $o3 = "off_472080" wide ascii nocase
    $o4 = "x2D6735AC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726175200_1904 {
  strings:
    $o0 = "off_47192C" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726175204_6209 {
  condition:
    auto_rule_20250726175157_7896 or auto_rule_20250726175200_1904
}