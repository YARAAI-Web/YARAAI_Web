rule auto_rule_20250727033443_9167 {
  strings:
    $o0 = "dword_650303E8" wide ascii nocase
    $o1 = "PipeAttributes" wide ascii nocase
  condition:
    all of them
}