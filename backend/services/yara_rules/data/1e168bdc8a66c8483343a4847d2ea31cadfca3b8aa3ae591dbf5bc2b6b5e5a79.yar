rule auto_rule_20250726194718_0691 {
  strings:
    $o0 = "dword_77F8C" wide ascii nocase
  condition:
    all of them
}