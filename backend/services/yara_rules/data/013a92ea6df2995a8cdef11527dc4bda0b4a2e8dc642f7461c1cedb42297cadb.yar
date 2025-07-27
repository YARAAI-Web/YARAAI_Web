rule auto_rule_20250726061148_1084 {
  strings:
    $o0 = "qword_1A6887215A0" wide ascii nocase
    $o1 = "qword_1A688721318" wide ascii nocase
  condition:
    all of them
}