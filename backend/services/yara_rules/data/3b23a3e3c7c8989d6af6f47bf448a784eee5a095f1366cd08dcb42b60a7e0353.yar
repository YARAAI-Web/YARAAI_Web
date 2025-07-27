rule auto_rule_20250726173105_4856 {
  strings:
    $o0 = "dword_4593FC" wide ascii nocase
    $o1 = "off_4587EC" wide ascii nocase
  condition:
    all of them
}