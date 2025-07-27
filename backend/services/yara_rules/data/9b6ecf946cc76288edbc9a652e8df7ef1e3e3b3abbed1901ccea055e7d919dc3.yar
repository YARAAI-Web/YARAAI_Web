rule auto_rule_20250727030540_6722 {
  strings:
    $o0 = "xE408" wide ascii nocase
    $o1 = "x8E09" wide ascii nocase
  condition:
    all of them
}