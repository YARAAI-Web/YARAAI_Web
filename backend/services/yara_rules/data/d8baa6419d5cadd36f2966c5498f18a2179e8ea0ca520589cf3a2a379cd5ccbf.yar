rule auto_rule_20250726074116_6882 {
  strings:
    $o0 = "dword_443F38" wide ascii nocase
    $o1 = "x1004u" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
    $o3 = "__ascii_strnicmp" wide ascii nocase
    $o4 = "dword_43D240" wide ascii nocase
  condition:
    4 of ($o*)
}