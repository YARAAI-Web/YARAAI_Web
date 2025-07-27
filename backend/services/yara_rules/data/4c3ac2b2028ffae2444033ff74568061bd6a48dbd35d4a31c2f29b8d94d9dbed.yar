rule auto_rule_20250727035743_1763 {
  strings:
    $o0 = "x6010" wide ascii nocase
    $o1 = "xF89C853B" wide ascii nocase
  condition:
    all of them
}