rule auto_rule_20250726114208_3920 {
  strings:
    $o0 = "qword_18012D838" wide ascii nocase
    $o1 = "p_Str1" wide ascii nocase
  condition:
    all of them
}