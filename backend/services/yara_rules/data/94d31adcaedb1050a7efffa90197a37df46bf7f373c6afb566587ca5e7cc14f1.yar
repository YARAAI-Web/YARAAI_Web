rule auto_rule_20250726210948_9760 {
  strings:
    $o0 = "dword_411D60" wide ascii nocase
    $o1 = "start_byte_3" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
  condition:
    3 of ($o*)
}