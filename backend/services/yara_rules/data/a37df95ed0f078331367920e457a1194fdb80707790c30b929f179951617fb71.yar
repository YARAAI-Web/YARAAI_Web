rule auto_rule_20250726204914_6348 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "byte_4698E0" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
    $o3 = "dword_469D3C" wide ascii nocase
  condition:
    4 of ($o*)
}