rule auto_rule_20250726154333_1478 {
  strings:
    $o0 = "qword_62751030" wide ascii nocase
  condition:
    all of them
}