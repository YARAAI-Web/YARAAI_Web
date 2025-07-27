rule auto_rule_20250726234531_4934 {
  strings:
    $o0 = "dword_1400D12D4" wide ascii nocase
    $o1 = "AllocConsole" wide ascii nocase
  condition:
    all of them
}