rule auto_rule_20250726074834_3404 {
  strings:
    $o0 = "_ms_p5_test_fdiv" wide ascii nocase
    $o1 = "xFF000000" wide ascii nocase
    $o2 = "_fassign" wide ascii nocase
    $o3 = "off_45648C" wide ascii nocase
    $o4 = "off_456484" wide ascii nocase
  condition:
    4 of ($o*)
}