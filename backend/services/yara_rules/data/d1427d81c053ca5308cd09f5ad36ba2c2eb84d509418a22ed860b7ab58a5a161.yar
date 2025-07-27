rule auto_rule_20250726195716_9448 {
  strings:
    $o0 = "x8C7u" wide ascii nocase
    $o1 = "dword_429173" wide ascii nocase
    $o2 = "x70941FE9" wide ascii nocase
  condition:
    3 of ($o*)
}