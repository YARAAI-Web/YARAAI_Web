rule auto_rule_20250727034001_9735 {
  strings:
    $o0 = "xFFFFFFFFFFFFFFF8uLL" wide ascii nocase
    $o1 = "xmmword_1800D0D78" wide ascii nocase
  condition:
    all of them
}