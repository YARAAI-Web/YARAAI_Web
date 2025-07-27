rule auto_rule_20250726064351_5862 {
  strings:
    $o0 = "dword_411B28" wide ascii nocase
    $o1 = "x_ismbbtype" wide ascii nocase
    $o2 = "_setenvp" wide ascii nocase
    $o3 = "dword_4119A0" wide ascii nocase
  condition:
    4 of ($o*)
}