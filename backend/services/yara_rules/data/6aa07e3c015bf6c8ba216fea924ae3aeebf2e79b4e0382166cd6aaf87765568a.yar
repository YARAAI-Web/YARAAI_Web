rule auto_rule_20250726160926_1978 {
  strings:
    $o0 = "dword_401328" wide ascii nocase
    $o1 = "VirtualAllocEx" wide ascii nocase
  condition:
    all of them
}