rule auto_rule_20250726181821_5182 {
  strings:
    $o0 = "dword_4071EC" wide ascii nocase
    $o1 = "launch4j" wide ascii nocase
  condition:
    all of them
}