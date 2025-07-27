rule auto_rule_20250726065139_2088 {
  strings:
    $o0 = "TrailDown0" wide ascii nocase
    $o1 = "xC000008F" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
    $o3 = "write_string" wide ascii nocase
    $o4 = "_aullrem" wide ascii nocase
  condition:
    5 of ($o*)
}