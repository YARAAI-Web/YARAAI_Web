rule auto_rule_20250726090358_8697 {
  strings:
    $o0 = "xF89F85B6" wide ascii nocase
  condition:
    all of them
}