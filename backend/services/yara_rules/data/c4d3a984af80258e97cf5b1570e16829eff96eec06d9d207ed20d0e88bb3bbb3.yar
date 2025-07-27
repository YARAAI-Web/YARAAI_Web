rule auto_rule_20250726235841_5362 {
  strings:
    $o0 = "dword_7AA034" wide ascii nocase
  condition:
    all of them
}