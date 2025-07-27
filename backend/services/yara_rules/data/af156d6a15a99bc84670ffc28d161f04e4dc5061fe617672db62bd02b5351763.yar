rule auto_rule_20250727010556_2163 {
  strings:
    $o0 = "dwMoveMethoda" wide ascii nocase
  condition:
    all of them
}