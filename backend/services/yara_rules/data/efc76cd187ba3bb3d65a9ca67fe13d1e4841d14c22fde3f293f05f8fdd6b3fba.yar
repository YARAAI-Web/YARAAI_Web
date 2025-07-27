rule auto_rule_20250726081817_4335 {
  strings:
    $o0 = "dword_42CA54" wide ascii nocase
    $o1 = "lfHeight" wide ascii nocase
    $o2 = "xFFFFFF" wide ascii nocase
    $o3 = "dword_416A0C" wide ascii nocase
  condition:
    4 of ($o*)
}