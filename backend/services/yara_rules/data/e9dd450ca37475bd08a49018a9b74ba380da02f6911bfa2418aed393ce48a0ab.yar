rule auto_rule_20250726071233_8099 {
  strings:
    $o0 = "x_ismbbtype" wide ascii nocase
    $o1 = "dword_445EE4" wide ascii nocase
    $o2 = "dword_445A34" wide ascii nocase
  condition:
    3 of ($o*)
}