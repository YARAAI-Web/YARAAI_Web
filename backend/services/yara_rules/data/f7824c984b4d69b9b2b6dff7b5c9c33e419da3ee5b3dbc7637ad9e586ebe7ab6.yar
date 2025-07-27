rule auto_rule_20250726205338_3478 {
  strings:
    $o0 = "qword_18026C868" wide ascii nocase
  condition:
    all of them
}