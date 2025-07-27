rule auto_rule_20250726075321_9106 {
  strings:
    $o0 = "plLength" wide ascii nocase
    $o1 = "dword_430020" wide ascii nocase
    $o2 = "safely" wide ascii nocase
  condition:
    3 of ($o*)
}