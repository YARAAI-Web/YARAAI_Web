rule auto_rule_20250726120007_2616 {
  strings:
    $o0 = "IsBadWritePtr" wide ascii nocase
    $o1 = "byte_4655A1" wide ascii nocase
    $o2 = "x157" wide ascii nocase
  condition:
    3 of ($o*)
}