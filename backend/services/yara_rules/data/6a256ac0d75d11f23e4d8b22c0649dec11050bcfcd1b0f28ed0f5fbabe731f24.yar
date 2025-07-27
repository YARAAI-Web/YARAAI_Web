rule auto_rule_20250726104820_2223 {
  strings:
    $o0 = "dword_46D570" wide ascii nocase
    $o1 = "IsBadWritePtr" wide ascii nocase
  condition:
    all of them
}