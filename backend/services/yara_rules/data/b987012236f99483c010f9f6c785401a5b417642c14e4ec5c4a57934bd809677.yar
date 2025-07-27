rule auto_rule_20250726221832_9884 {
  strings:
    $o0 = "dword_469A00" wide ascii nocase
    $o1 = "off_469678" wide ascii nocase
  condition:
    all of them
}