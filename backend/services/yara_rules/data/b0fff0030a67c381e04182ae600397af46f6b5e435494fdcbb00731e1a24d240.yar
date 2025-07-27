rule auto_rule_20250726210241_9519 {
  strings:
    $o0 = "x2FA6" wide ascii nocase
    $o1 = "dword_43060E" wide ascii nocase
    $o2 = "x5250" wide ascii nocase
  condition:
    3 of ($o*)
}