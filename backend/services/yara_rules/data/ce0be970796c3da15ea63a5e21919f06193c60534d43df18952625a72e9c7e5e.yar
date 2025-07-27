rule auto_rule_20250726203906_6540 {
  strings:
    $o0 = "qword_140025A18" wide ascii nocase
  condition:
    all of them
}