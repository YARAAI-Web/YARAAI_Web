rule auto_rule_20250726072127_4649 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "byte_407B50" wide ascii nocase
    $o2 = "nProgram" wide ascii nocase
    $o3 = "x_ismbbtype" wide ascii nocase
    $o4 = "byte_411C21" wide ascii nocase
  condition:
    4 of ($o*)
}