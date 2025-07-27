rule auto_rule_20250726190805_8536 {
  strings:
    $o0 = "hReadPipe" wide ascii nocase
    $o1 = "dword_6502E168" wide ascii nocase
  condition:
    all of them
}