rule auto_rule_20250726201907_5319 {
  strings:
    $o0 = "off_49BD88" wide ascii nocase
    $o1 = "off_49B7E8" wide ascii nocase
    $o2 = "aCalledOptionUn" wide ascii nocase
  condition:
    3 of ($o*)
}