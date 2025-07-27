rule auto_rule_20250726105340_1412 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "x_ismbbtype" wide ascii nocase
    $o2 = "UnwindUp6_0" wide ascii nocase
    $o3 = "TargetIp" wide ascii nocase
    $o4 = "off_427524" wide ascii nocase
  condition:
    5 of ($o*)
}