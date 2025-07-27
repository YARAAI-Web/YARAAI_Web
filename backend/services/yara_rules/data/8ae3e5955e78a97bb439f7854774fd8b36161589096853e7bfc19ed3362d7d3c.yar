rule auto_rule_20250726160724_4166 {
  strings:
    $o0 = "DrawDibOpen" wide ascii nocase
    $o1 = "dword_460138" wide ascii nocase
  condition:
    all of them
}