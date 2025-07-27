rule auto_rule_20250726201205_2233 {
  strings:
    $o0 = "off_41B1A8" wide ascii nocase
    $o1 = "x8A3E" wide ascii nocase
    $o2 = "dword_41B224" wide ascii nocase
    $o3 = "x4B6B" wide ascii nocase
  condition:
    4 of ($o*)
}