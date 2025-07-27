rule auto_rule_20250726194837_9210 {
  strings:
    $o0 = "dword_45B014" wide ascii nocase
  condition:
    all of them
}