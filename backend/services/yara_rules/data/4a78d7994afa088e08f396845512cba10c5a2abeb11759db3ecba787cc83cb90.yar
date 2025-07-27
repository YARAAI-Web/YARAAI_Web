rule auto_rule_20250727011032_5021 {
  strings:
    $o0 = "xFFFFFFFFFEFFFFFFuLL" wide ascii nocase
  condition:
    all of them
}