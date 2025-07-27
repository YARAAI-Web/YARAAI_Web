rule auto_rule_20250726164505_4631 {
  strings:
    $o0 = "x_ismbbtype" wide ascii nocase
    $o1 = "dword_451168" wide ascii nocase
    $o2 = "dword_4514EC" wide ascii nocase
    $o3 = "off_450CA8" wide ascii nocase
    $o4 = "strcspn" wide ascii nocase
  condition:
    4 of ($o*)
}