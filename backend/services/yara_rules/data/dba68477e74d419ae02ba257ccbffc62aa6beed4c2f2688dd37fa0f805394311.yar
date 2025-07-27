rule auto_rule_20250726231308_5500 {
  strings:
    $o0 = "ymm0" wide ascii nocase
    $o1 = "C00Ch" wide ascii nocase
  condition:
    all of them
}