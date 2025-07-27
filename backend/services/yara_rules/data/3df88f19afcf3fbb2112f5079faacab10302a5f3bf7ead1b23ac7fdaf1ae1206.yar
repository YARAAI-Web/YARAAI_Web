rule auto_rule_20250726063035_2167 {
  strings:
    $o0 = "dword_44A3A4" wide ascii nocase
    $o1 = "byte_44A181" wide ascii nocase
    $o2 = "dword_44A3B8" wide ascii nocase
    $o3 = "TrailUp3" wide ascii nocase
    $o4 = "x_ismbbtype" wide ascii nocase
  condition:
    4 of ($o*)
}