rule auto_rule_20250727021110_2205 {
  strings:
    $o0 = "dword_45CAD8" wide ascii nocase
    $o1 = "byte_45CC14" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
  condition:
    3 of ($o*)
}