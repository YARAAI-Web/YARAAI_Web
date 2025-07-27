rule auto_rule_20250726165542_9571 {
  strings:
    $o0 = "dword_477188" wide ascii nocase
    $o1 = "dword_477308" wide ascii nocase
  condition:
    all of them
}