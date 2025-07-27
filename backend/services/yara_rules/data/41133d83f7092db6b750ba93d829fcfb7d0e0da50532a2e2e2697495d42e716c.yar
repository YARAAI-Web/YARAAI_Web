rule auto_rule_20250726211705_4198 {
  strings:
    $o0 = "asserts" wide ascii nocase
    $o1 = "byte_468E81" wide ascii nocase
  condition:
    all of them
}