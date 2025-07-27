rule auto_rule_20250726124358_1320 {
  strings:
    $o0 = "qword_1811CB2D8" wide ascii nocase
    $o1 = "qword_180B4F838" wide ascii nocase
    $o2 = "qword_1811CB640" wide ascii nocase
    $o3 = "qword_1811CB498" wide ascii nocase
  condition:
    4 of ($o*)
}