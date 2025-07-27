rule auto_rule_20250726063906_2200 {
  strings:
    $o0 = "dword_4C173C" wide ascii nocase
  condition:
    all of them
}