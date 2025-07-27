rule auto_rule_20250726142757_0948 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "dword_463E04" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
    $o3 = "dword_4647D0" wide ascii nocase
  condition:
    4 of ($o*)
}