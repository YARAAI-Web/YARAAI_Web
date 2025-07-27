rule auto_rule_20250726141020_1559 {
  strings:
    $o0 = "x8E12FEB8" wide ascii nocase
    $o1 = "aL748wi5P" wide ascii nocase
    $o2 = "x5E17" wide ascii nocase
    $o3 = "yBottom" wide ascii nocase
    $o4 = "x66DB" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726141023_0017 {
  strings:
    $o0 = "x3FA4" wide ascii nocase
    $o1 = "iCharSet" wide ascii nocase
    $o2 = "off_413C08" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726141027_3295 {
  condition:
    auto_rule_20250726141020_1559 or auto_rule_20250726141023_0017
}