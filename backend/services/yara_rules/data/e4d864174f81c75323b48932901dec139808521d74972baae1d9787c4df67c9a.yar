rule auto_rule_20250726204109_1466 {
  strings:
    $o0 = "should" wide ascii nocase
    $o1 = "qword_140043E58" wide ascii nocase
    $o2 = "x1070u" wide ascii nocase
    $o3 = "qword_140043ED0" wide ascii nocase
  condition:
    4 of ($o*)
}