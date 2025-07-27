rule auto_rule_20250726121700_9796 {
  strings:
    $o0 = "x404791" wide ascii nocase
    $o1 = "dword_4692E0" wide ascii nocase
    $o2 = "__termcon" wide ascii nocase
    $o3 = "x_ismbbtype" wide ascii nocase
  condition:
    4 of ($o*)
}