rule auto_rule_20250726061340_9197 {
  strings:
    $o0 = "dword_4849CC" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
  condition:
    all of them
}